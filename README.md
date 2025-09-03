# FORMS Edge Delivery MCP Toolkit

A comprehensive Model Context Protocol (MCP) toolkit for Adobe Experience Manager FORMS Edge Delivery development, providing styling tools, documentation, and prompts for form components across both Python and Node.js environments.

## 🌟 Overview

This repository contains two MCP implementations that provide access to FORMS Edge Delivery styling tools and documentation:

- **🐍 Python MCP Server** (`forms-edge-delivery-mcp`) - Core server with 11 tools, 2 resources, and 13 styling prompts
- **📦 Node.js MCP Client** (`@formsedsmcp/forms-edge-delivery-mcp-nodejs`) - Proxy server that connects to the Python server via HTTP

Both implementations support integration with AI assistants like Claude Desktop, Cursor IDE, and other MCP-compatible clients.

## 🐍 Python MCP Server (forms-edge-delivery-mcp)

### About the Python MCP Server

The Python MCP server is the core implementation providing all FORMS Edge Delivery styling tools and documentation. It supports both **HTTP** and **STDIO** transports, making it flexible for different integration scenarios.

## For Development
1. **Clone repository:**
   ```bash
   git clone <repository-url>
   cd agent
   ```

2. **Install Python server:**
   ```bash
   cd mcp
   pip install -e .
   ```
3. **Start in http mode**
   ```bash
   MCP_TRANSPORT=http MCP_PORT=8080 MCP_HOST=localhost MCP_DEBUG=false forms-edge-delivery-mcp
   ```
   
4. **Start in stdio mode (Recommended for coding agents)**
   ```bash
   MCP_TRANSPORT=stdio  MCP_DEBUG=false forms-edge-delivery-mcp
   ```
**You can also change the values of these environment variables in .env file**   


## For Development (Using docker)
The docker-compose.yml file already has environment variables configured to run the mcp server over http on port 8080
```bash
cd mcp
docker-compose down && docker-compose up --build -d
```


## 🏗️ Architecture

```
┌─────────────────┐    MCP Protocol    ┌─────────────────┐    HTTP/STDIO    ┌─────────────────┐
│   MCP Client    │ ◄─────────────────► │  Node.js Proxy │ ◄───────────────► │  Python Server  │
│ (Claude, Cursor)│                     │     Server      │                   │   (FastAPI)     │
└─────────────────┘                     └─────────────────┘                   └─────────────────┘

                                                   OR

┌─────────────────┐    MCP Protocol (STDIO)      ┌─────────────────────────────────────────────────┐
│   MCP Client    │ ◄─────────────────────────────│          Python Server Direct                  │
│ (Claude, Cursor)│                               │              (FastMCP)                          │
└─────────────────┘                               └─────────────────────────────────────────────────┘
```

## 🛠️ Available Tools & Features

### 📋 MCP Tools (11 tools)
- **Field Structure Styling** - HTML structure and CSS for form fields
- **Dropdown Styling** - Modern dropdown component styling
- **Radio/Checkbox Styling** - Custom-styled radio buttons and checkboxes
- **Panel Container Styling** - Panel and container layouts
- **CSS Selectors Guide** - Comprehensive CSS selector targeting
- **File Attachment Styling** - File upload components with drag-and-drop
- **Error Message Styling** - Form validation and error displays
- **Repeatable Panel Styling** - Dynamic repeatable form sections
- **Custom Component Creation** - Advanced component decorators
- **Layout Configuration** - Wizard, accordion, tabs layouts
- **System Information** - Server details and environment info

### 📚 Resources (2 resources)
- **Server Info** - MCP server details and capabilities
- **System Info** - Platform and environment information

### 💡 Styling Prompts (13 prompts)
- CSS selector mastery techniques
- Modern form component styling
- Error state visual design
- Advanced layout patterns
- Complete form theming strategies
- Animation and visual effects

---

## 📦 How to use this mcp in your node js project

### About the Node.js MCP Client

The Node.js MCP client (`@formsedsmcp/forms-edge-delivery-mcp-nodejs`) is a lightweight proxy server that forwards MCP requests to the Python server via HTTP. This allows Node.js applications and MCP clients to access all FORMS styling tools through a native Node.js interface.

### 🚀 Adding to Your npm Project in Cursor


#### Step 1: Install the Package

Start the mcp server in http mode

```bash
# Install from npm registry
npm install @formsedsmcp/forms-edge-delivery-mcp-nodejs

# Or using yarn
yarn add @formsedsmcp/forms-edge-delivery-mcp-nodejs
```

#### Step 2: Configure for Cursor IDE

Create or update your Cursor MCP configuration file:

**File:** `.cursor/mcp.json` or your Cursor settings

```json
{
  "mcpServers": {
    "forms-eds-mcp-nodejs": {
      "command": "node",
      "args": ["./node_modules/@formsedsmcp/forms-edge-delivery-mcp-nodejs/src/server.js"],
      "env": {
        "MCP_SERVER_URL": "http://localhost:8080",
        "HTTP_TIMEOUT": 30000,
        "DEBUG": "false"
      }
    }
  }
}
```



## 📦 How to use this mcp in your node js project

### build the mcp 
```bash

source agent/mcp-env/bin/activate
cd mcp
pip install -e .
python3 -m build
```
This will build your wheel and tar files in dist/ folder

## start a local Pypi Server
```bash
 pypi-server run -p 8081 dist/
```
## Install the Package

```bash
# Install from local PyPI 
pip install --index-url http://localhost:8081/simple forms-edge-delivery-mcp
```

## Add in your mcp.json
```json
{
  "mcpServers": {
    "forms-edge-delivery-mcp": {
      "command": "/Users/deepprakashdewanji/codebases/pythonproject/pythonproject/bin/forms-edge-delivery-mcp",
      "args": [],
      "env": {
        "MCP_TRANSPORT": "stdio"
      }
    }
  }
}

``` 




## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

MIT License - see LICENSE file for details.

## 🆘 Support & Documentation

- **Issues:** GitHub Issues
- **Documentation:** Available through MCP tools and prompts

---

*This toolkit provides comprehensive FORMS Edge Delivery styling support for modern AI-assisted development workflows.*
