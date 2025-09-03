/**
 * HTTP Client for communicating with Python MCP Server
 */

import fetch from 'node-fetch';
import { CONFIG } from './config.js';

export class HttpClient {
  constructor() {
    this.baseUrl = CONFIG.mcp_server.base_url;
    this.timeout = CONFIG.mcp_server.timeout;
  }

  /**
   * Make a POST request to the Python MCP server
   * @param {string} endpoint - The endpoint path (e.g., '/field-structure')
   * @param {Object} data - Optional request body data
   * @returns {Promise<Object>} - The response from the Python server
   */
  async post(endpoint, data = {}) {
    const url = `${this.baseUrl}${endpoint}`;
    
    if (CONFIG.debug) {
      console.log(`🔗 Making request to: ${url}`);
      console.log(`📤 Request data:`, data);
    }

    try {
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), this.timeout);

      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'User-Agent': 'FORMS-Edge-Delivery-MCP-NodeJS/1.0.0'
        },
        body: JSON.stringify(data),
        signal: controller.signal
      });

      clearTimeout(timeoutId);

      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`);
      }

      const result = await response.json();
      
      if (CONFIG.debug) {
        console.log(`📥 Response status:`, result.status);
        console.log(`📥 Response preview:`, result.data?.substring(0, 200) + '...');
      }

      return result;
    } catch (error) {
      if (error.name === 'AbortError') {
        throw new Error(`Request timeout after ${this.timeout}ms`);
      }
      
      console.error(`❌ Request failed for ${endpoint}:`, error.message);
      throw new Error(`Failed to communicate with Python MCP server: ${error.message}`);
    }
  }

  /**
   * Check if the Python MCP server is healthy
   * @returns {Promise<boolean>} - True if server is healthy
   */
  async healthCheck() {
    try {
      const response = await fetch(`${this.baseUrl}/health`, {
        method: 'GET',
        timeout: 5000
      });
      return response.ok;
    } catch (error) {
      if (CONFIG.debug) {
        console.error('❌ Health check failed:', error.message);
      }
      return false;
    }
  }

  /**
   * Get server information
   * @returns {Promise<Object>} - Server information
   */
  async getServerInfo() {
    try {
      const response = await fetch(`${this.baseUrl}/resource/server-info`, {
        method: 'GET',
        timeout: 5000
      });
      
      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`);
      }
      
      return await response.json();
    } catch (error) {
      throw new Error(`Failed to get server info: ${error.message}`);
    }
  }

  /**
   * Get system information
   * @returns {Promise<Object>} - System information
   */
  async getSystemInfo() {
    try {
      const response = await fetch(`${this.baseUrl}/resource/system-info`, {
        method: 'GET',
        timeout: 5000
      });
      
      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`);
      }
      
      return await response.json();
    } catch (error) {
      throw new Error(`Failed to get system info: ${error.message}`);
    }
  }
}

export default HttpClient;
