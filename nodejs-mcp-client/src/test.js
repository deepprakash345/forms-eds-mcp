#!/usr/bin/env node

/**
 * Test script for Node.js MCP Proxy Server
 */

import PythonMCPClient from './http-client.js';
import { CONFIG } from './config.js';
import { getPrompts } from './prompts.js';

async function testPythonServer() {
  console.log('🧪 Testing Node.js MCP Proxy Server');
  console.log('=' .repeat(50));
  
  const client = new PythonMCPClient();
  
  // Test 1: Health Check
  console.log('\n1️⃣ Testing Python server health check...');
  try {
    const isHealthy = await client.healthCheck();
    console.log(`   Health status: ${isHealthy ? '✅ Healthy' : '❌ Unhealthy'}`);
  } catch (error) {
    console.log(`   Health check failed: ❌ ${error.message}`);
  }
  
  // Test 2: Server Info
  console.log('\n2️⃣ Testing server info...');
  try {
    const serverInfo = await client.getServerInfo();
    console.log(`   Server: ${serverInfo.name} v${serverInfo.version}`);
    console.log(`   Status: ✅ Success`);
  } catch (error) {
    console.log(`   Server info failed: ❌ ${error.message}`);
  }
  
  // Test 3: Sample Tool Calls
  console.log('\n3️⃣ Testing sample tool calls...');
  
  const testEndpoints = [
    { name: 'System Info', endpoint: '/system-info' },
    { name: 'Field Structure', endpoint: '/field-structure' },
    { name: 'Layout Configuration', endpoint: '/layout-configuration' }
  ];
  
  for (const test of testEndpoints) {
    console.log(`\n   Testing ${test.name}...`);
    try {
      const result = await client.post(test.endpoint);
      console.log(`   Status: ${result.status === 'success' ? '✅' : '❌'} ${result.status}`);
      console.log(`   Data length: ${result.data ? result.data.length : 0} characters`);
      if (result.errorMessage) {
        console.log(`   Error: ${result.errorMessage}`);
      }
    } catch (error) {
      console.log(`   Request failed: ❌ ${error.message}`);
    }
  }
  
  // Test 4: Prompts Check
  console.log('\n4️⃣ Prompts check...');
  const prompts = getPrompts();
  console.log(`   Available prompts: ${prompts.length}`);
  console.log(`   Sample prompts: ${prompts.slice(0, 3).map(p => p.name).join(', ')}`);
  
  // Test 5: Configuration
  console.log('\n5️⃣ Configuration check...');
  console.log(`   Python server URL: ${CONFIG.mcp_server.base_url}`);
  console.log(`   Timeout: ${CONFIG.mcp_server.timeout}ms`);
  console.log(`   Available endpoints: ${Object.keys(CONFIG.endpoints).length}`);
  console.log(`   Debug mode: ${CONFIG.debug ? 'ON' : 'OFF'}`);
  
  console.log('\n' + '=' .repeat(50));
  console.log('🎉 Test completed!');
  console.log('\n💡 To start the MCP server, run: npm start');
  console.log('💡 To enable debug mode, set: DEBUG=true npm start');
}

// Run tests
testPythonServer().catch(console.error);
