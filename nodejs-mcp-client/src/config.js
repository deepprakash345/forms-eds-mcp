/**
 * Configuration for Node.js MCP Proxy Server
 */

// Load environment variables from .env file if it exists
import dotenv from 'dotenv';
dotenv.config();

export const CONFIG = {
  // Python MCP Server Configuration
  mcp_server: {
    base_url: process.env.MCP_SERVER_URL || 'http://localhost:8080',
    timeout: parseInt(process.env.HTTP_TIMEOUT) || 30000
  },
  
  // Node.js MCP Server Configuration
  server: {
    name: 'FORMS Edge Delivery MCP Proxy (Node.js)',
    version: '1.0.0',
    description: 'Node.js MCP server that proxies to Python FORMS Edge Delivery MCP server via HTTP'
  },
  
  // HTTP endpoints mapping
  endpoints: {
    'get_field_structure_styling': '/field-structure',
    'get_dropdown_styling': '/dropdown-styling', 
    'get_radio_checkbox_styling': '/radio-checkbox-styling',
    'get_panel_container_styling': '/panel-container-styling',
    'get_css_selectors_guide': '/css-selectors-guide',
    'get_file_attachment_styling': '/file-attachment-styling',
    'get_error_message_styling': '/error-message-styling',
    'get_repeatable_panel_styling': '/repeatable-panel-styling',
    'get_custom_component_creation': '/custom-component-creation',
    'get_layout_configuration': '/layout-configuration',
    'get_system_information': '/system-info'
  },

  // Debug mode
  debug: process.env.DEBUG === 'true' || process.env.MCP_DEBUG === 'true'
};

export default CONFIG;
