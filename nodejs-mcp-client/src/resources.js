/**
 * Resources definitions for FORMS Edge Delivery MCP Server
 */

/**
 * Get available resources
 * @returns {Array} Array of resource definitions
 */
export function getResources() {
  return [
    {
      uri: 'server-info',
      name: 'Server Information',
      description: 'Information about the FORMS Edge Delivery MCP server itself',
      mimeType: 'application/json'
    },
    {
      uri: 'system-info', 
      name: 'System Information',
      description: 'System and environment information for the server',
      mimeType: 'application/json'
    }
  ];
}

export default getResources;
