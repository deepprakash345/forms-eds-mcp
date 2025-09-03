#!/usr/bin/env node

/**
 * Node.js MCP Server that proxies to Python FORMS Edge Delivery MCP Server via HTTP
 */

import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
  ListResourcesRequestSchema,
  ReadResourceRequestSchema,
  ListPromptsRequestSchema,
  GetPromptRequestSchema,
} from '@modelcontextprotocol/sdk/types.js';

import { CONFIG } from './config.js';
import HttpClient from './http-client.js';
import { getTools } from './tools.js';
import { getResources } from './resources.js';
import { getPrompts } from './prompts.js';

/**
 * Create and configure the MCP server
 */
class FormsMCPProxyServer {
  constructor() {
    this.server = new Server(
      {
        name: CONFIG.server.name,
        version: CONFIG.server.version,
      },
      {
        capabilities: {
          tools: {},
          resources: {},
          prompts: {},
        },
      }
    );
    
    this.client = new HttpClient();
    this.setupHandlers();
  }

  setupHandlers() {
    // List available tools
    this.server.setRequestHandler(ListToolsRequestSchema, async () => {
      return {
        tools: getTools()
      };
    });

    this.server.setRequestHandler(ListResourcesRequestSchema, async () => {
      return {
        resources: getResources()
      };
    });

    // List available prompts
    this.server.setRequestHandler(ListPromptsRequestSchema, async () => {
      return {
        prompts: getPrompts()
      };
    });

    // Handle prompt requests
    this.server.setRequestHandler(GetPromptRequestSchema, async (request) => {
      const { name, arguments: args } = request.params;
      
      if (CONFIG.debug) {
        console.log(`💬 Prompt requested: ${name}`);
        console.log(`📊 Arguments:`, args);
      }

      // Find the prompt by name
      const prompts = getPrompts();
      const prompt = prompts.find(p => p.name === name);
      
      if (!prompt) {
        throw new Error(`Unknown prompt: ${name}`);
      }

      // Return the prompt content
      return {
        description: prompt.description,
        messages: [
          {
            role: 'user',
            content: {
              type: 'text',
              text: prompt.prompt
            }
          }
        ]
      };
    });

    // Handle resource reads
    this.server.setRequestHandler(ReadResourceRequestSchema, async (request) => {
      const { uri } = request.params;
      
      if (CONFIG.debug) {
        console.log(`📖 Resource requested: ${uri}`);
      }

      try {
        let result;
        
        switch (uri) {
          case 'server-info':
            result = await this.client.getServerInfo();
            break;
          case 'system-info':
            result = await this.client.getSystemInfo();
            break;
          default:
            throw new Error(`Unknown resource: ${uri}`);
        }

        // Return the result in MCP resource format
        return {
          contents: [
            {
              uri: uri,
              mimeType: 'application/json',
              text: JSON.stringify(result, null, 2)
            }
          ]
        };
      } catch (error) {
        console.error(`❌ Resource read failed for ${uri}:`, error.message);
        throw new Error(`Failed to read resource ${uri}: ${error.message}`);
      }
    });

    // Handle tool calls
    this.server.setRequestHandler(CallToolRequestSchema, async (request) => {
      const { name, arguments: args } = request.params;
      
      if (CONFIG.debug) {
        console.log(`🔧 Tool called: ${name}`);
        console.log(`📊 Arguments:`, args);
      }

      // Check if we have a mapping for this tool
      const endpoint = CONFIG.endpoints[name];
      if (!endpoint) {
        throw new Error(`Unknown tool: ${name}`);
      }

      try {
        // Make request to Python server
        const result = await this.client.post(endpoint, args || {});
        
        // Return the result in MCP format
        return {
          content: [
            {
              type: 'text',
              text: result.data || result.errorMessage || 'No data received'
            }
          ]
        };
      } catch (error) {
        console.error(`❌ Tool execution failed for ${name}:`, error.message);
        
        return {
          content: [
            {
              type: 'text', 
              text: `Error: ${error.message}`
            }
          ],
          isError: true
        };
      }
    });
  }

  async start() {
    // Check Python server health before starting
    if (CONFIG.debug) {
      console.log(`🔍 Checking Python server health at ${CONFIG.python_server.base_url}...`);
      const isHealthy = await this.client.healthCheck();
      
      if (isHealthy) {
        console.log(`✅ Python server is healthy`);
        try {
          const serverInfo = await this.client.getServerInfo();
          console.log(`📊 Python server: ${serverInfo.name} v${serverInfo.version}`);
        } catch (error) {
          console.log(`⚠️  Could not get server info: ${error.message}`);
        }
      } else {
        console.log(`⚠️  Python server health check failed - continuing anyway`);
      }
    }

    // Start the MCP server
    const transport = new StdioServerTransport();
    await this.server.connect(transport);
    
    if (CONFIG.debug) {
      console.log(`🚀 Node.js MCP Proxy Server started`);
      console.log(`📡 Proxying to: ${CONFIG.mcp_server.base_url}`);
      console.log(`🛠️  Available tools: ${getTools().length}`);
      console.log(`📚 Available resources: ${getResources().length} (${getResources().map(r => r.uri).join(', ')})`);
      console.log(`💬 Available prompts: ${getPrompts().length} (${getPrompts().map(p => p.name).join(', ')})`);
    }
  }
}

/**
 * Main execution
 */
async function main() {
  const server = new FormsMCPProxyServer();
  
  // Handle graceful shutdown
  process.on('SIGINT', async () => {
    if (CONFIG.debug) {
      console.log('\n🛑 Shutting down Node.js MCP Proxy Server...');
    }
    process.exit(0);
  });

  process.on('SIGTERM', async () => {
    if (CONFIG.debug) {
      console.log('\n🛑 Shutting down Node.js MCP Proxy Server...');
    }
    process.exit(0);
  });

  try {
    await server.start();
  } catch (error) {
    console.error('❌ Failed to start server:', error);
    process.exit(1);
  }
}

// Run the server
if (import.meta.url === `file://${process.argv[1]}`) {
  main().catch(console.error);
}
