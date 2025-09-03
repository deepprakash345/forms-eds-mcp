"""
FORMS Edge Delivery MCP Server with FastMCP
FORMS Edge Delivery MCP server providing tools and services for edge delivery operations
"""
from fastmcp import FastMCP
import json
import os
from .resources.system import get_server_info, get_system_info
from .config import SERVER_CONFIG

# Import managers for HTTP endpoints
from .managers.field_structure_manager import get_field_structure_styling
from .managers.dropdown_manager import get_dropdown_styling as dropdown_styling_manager
from .managers.radio_checkbox_manager import get_radio_checkbox_styling as radio_checkbox_styling_manager
from .managers.panel_container_manager import get_panel_container_styling as panel_container_styling_manager
from .managers.css_selectors_manager import get_css_selectors_guide as css_selectors_guide_manager
from .managers.file_attachment_manager import get_file_attachment_styling as file_attachment_styling_manager
from .managers.error_message_manager import get_error_message_styling as error_message_styling_manager
from .managers.repeatable_panel_manager import get_repeatable_panel_styling as repeatable_panel_styling_manager
from .managers.custom_component_manager import get_custom_component_creation as custom_component_creation_manager
from .managers.layout_manager import get_layout_configuration as layout_configuration_manager
from .managers.system_info_manager import get_system_information

# Import tool registration functions

from .tools.field_structure_tools import register_field_structure_tools
from .tools.dropdown_tools import register_dropdown_tools
from .tools.radio_checkbox_tools import register_radio_checkbox_tools
from .tools.panel_container_tools import register_panel_container_tools
from .tools.css_selectors_tools import register_css_selectors_tools
from .tools.file_attachment_tools import register_file_attachment_tools
from .tools.error_message_tools import register_error_message_tools
from .tools.repeatable_panel_tools import register_repeatable_panel_tools
from .tools.custom_component_tools import register_custom_component_tools
from .tools.layout_tools import register_layout_tools
from .tools.system_info_tools import register_system_info_tools

# Import prompt registration functions
from .prompts import register_all_prompts



# Debug setup - enable remote debugging if debug mode is on
if os.getenv('MCP_DEBUG', 'false').lower() == 'true' or os.getenv('DEBUG', 'false').lower() == 'true':
    try:
        import debugpy
        print("🐛 Debug mode detected - Starting debugpy on port 5678")
        try:
            debugpy.listen(("0.0.0.0", 5678))
            print("🔗 Waiting for debugger to attach on port 5678...")
        except RuntimeError as e:
            if "listen() has already been called" in str(e):
                print("🔗 debugpy already listening - continuing...")
            else:
                raise e
    except ImportError:
        print("⚠️  debugpy not installed - install with: pip install debugpy")
    except Exception as e:
        print(f"⚠️  Debug setup failed: {e}")




# Initialize the MCP server
mcp = FastMCP(
    name=SERVER_CONFIG["name"],
    version=SERVER_CONFIG["version"]
)

# Register all MCP tools (defined in tools/* modules)
register_system_info_tools(mcp)
register_field_structure_tools(mcp)
register_dropdown_tools(mcp)
register_radio_checkbox_tools(mcp)
register_panel_container_tools(mcp)
register_css_selectors_tools(mcp)
register_file_attachment_tools(mcp)
register_error_message_tools(mcp)
register_repeatable_panel_tools(mcp)
register_custom_component_tools(mcp)
register_layout_tools(mcp)

# Register prompt tools and resources
register_all_prompts(mcp)


# =============================================================================
# RESOURCES
# =============================================================================

@mcp.resource("resource://server-info")
def server_info_resource():
    """Provides information about the MCP server"""
    return get_server_info()

@mcp.resource("resource://system-info") 
def system_info_resource():
    """Provides system information"""
    return get_system_info()

# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    """Main entry point for the MCP server"""
    print(f"🚀 Starting {SERVER_CONFIG['name']} v{SERVER_CONFIG['version']}")
    print(f"📡 Transport: {SERVER_CONFIG['transport']}")
    
    if SERVER_CONFIG['transport'] == 'http':
        print(f"🌐 HTTP Server: {SERVER_CONFIG['host']}:{SERVER_CONFIG['port']}")
    
    if SERVER_CONFIG['debug']:
        print("🐛 Debug mode enabled")
    print("=" * 50)
    
    # Configure transport based on settings
    if SERVER_CONFIG['transport'] == 'http':
        # HTTP transport for Docker/API usage
        import uvicorn
        from fastapi import FastAPI
        from fastapi.middleware.cors import CORSMiddleware
        
        # Create FastAPI app for HTTP transport
        app = FastAPI(
            title=SERVER_CONFIG['name'],
            version=SERVER_CONFIG['version'],
            description=SERVER_CONFIG['description']
        )
        
        # Add CORS middleware
        app.add_middleware(
            CORSMiddleware,
            allow_origins=SERVER_CONFIG['allowed_origins'],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        
        # Health check endpoint
        @app.get("/health")
        async def health_check():
            return {"status": "healthy", "server": SERVER_CONFIG['name']}
        
        # HTTP endpoints using managers directly
        @app.post("/field-structure")
        async def api_field_structure():
            result = get_field_structure_styling()
            return json.loads(result)
            
        @app.post("/dropdown-styling")
        async def api_dropdown_styling():
            result = dropdown_styling_manager()
            return json.loads(result)
            
        @app.post("/radio-checkbox-styling")
        async def api_radio_checkbox_styling():
            result = radio_checkbox_styling_manager()
            return json.loads(result)
            
        @app.post("/panel-container-styling")
        async def api_panel_container_styling():
            result = panel_container_styling_manager()
            return json.loads(result)
            
        @app.post("/css-selectors-guide")
        async def api_css_selectors_guide():
            result = css_selectors_guide_manager()
            return json.loads(result)
            
        @app.post("/file-attachment-styling")
        async def api_file_attachment_styling():
            result = file_attachment_styling_manager()
            return json.loads(result)
            
        @app.post("/error-message-styling")
        async def api_error_message_styling():
            result = error_message_styling_manager()
            return json.loads(result)
            
        @app.post("/repeatable-panel-styling")
        async def api_repeatable_panel_styling():
            result = repeatable_panel_styling_manager()
            return json.loads(result)
            
        @app.post("/custom-component-creation")
        async def api_custom_component_creation():
            result = custom_component_creation_manager()
            return json.loads(result)
            
        @app.post("/layout-configuration")
        async def api_layout_configuration():
            result = layout_configuration_manager()
            return json.loads(result)
            
        @app.post("/system-info")
        async def api_system_info():
            result = get_system_information()
            return json.loads(result)

        # MCP Resource endpoints accessible via HTTP
        @app.get("/resource/server-info")
        async def api_server_info():
            return get_server_info()
            
        @app.get("/resource/system-info")
        async def api_resource_system_info():
            return get_system_info()

        # ==========================================
        # 🔍 API DISCOVERY ENDPOINTS
        # ==========================================
        
        @app.get("/")
        async def root():
            """Root endpoint with basic server info and links to discovery endpoints"""
            return {
                "name": "FORMS Edge Delivery MCP Server",
                "version": "1.0.0",
                "status": "running",
                "description": "MCP server providing FORMS styling and structure data",
                "discovery": {
                    "endpoints": "http://localhost:8080/api/discovery",
                    "schema": "http://localhost:8080/api/schema",
                    "health": "http://localhost:8080/health"
                },
                "documentation": "All endpoints return JSON data for FORMS Edge Delivery styling"
            }

        @app.get("/api/discovery")
        async def api_discovery():
            """Discover all available API endpoints"""
            return {
                "server": {
                    "name": "FORMS Edge Delivery MCP Server",
                    "version": "1.0.0",
                    "description": "Provides styling data and structure information for Adobe Experience Manager FORMS Edge Delivery"
                },
                "endpoints": {
                    "health": {
                        "method": "GET",
                        "path": "/health",
                        "description": "Server health check",
                        "returns": "Server status and basic info"
                    },
                    "serverInfo": {
                        "method": "GET", 
                        "path": "/resource/server-info",
                        "description": "Detailed server information",
                        "returns": "Server details and capabilities"
                    },
                    "systemInfo": {
                        "method": "GET",
                        "path": "/resource/system-info", 
                        "description": "System information",
                        "returns": "System details and environment info"
                    },
                    "fieldStructure": {
                        "method": "POST",
                        "path": "/field-structure",
                        "description": "Get field structure styling and markup patterns",
                        "returns": "HTML structure and CSS for form fields"
                    },
                    "dropdownStyling": {
                        "method": "POST",
                        "path": "/dropdown-styling",
                        "description": "Get dropdown component styling",
                        "returns": "CSS and HTML for dropdown elements"
                    },
                    "radioCheckboxStyling": {
                        "method": "POST", 
                        "path": "/radio-checkbox-styling",
                        "description": "Get radio button and checkbox styling",
                        "returns": "CSS and HTML for radio/checkbox elements"
                    },
                    "panelContainerStyling": {
                        "method": "POST",
                        "path": "/panel-container-styling", 
                        "description": "Get panel and container styling",
                        "returns": "CSS and HTML for panels and containers"
                    },
                    "cssSelectorsGuide": {
                        "method": "POST",
                        "path": "/css-selectors-guide",
                        "description": "Get CSS selectors guide for FORMS",
                        "returns": "Complete guide to CSS selectors for form styling"
                    },
                    "fileAttachmentStyling": {
                        "method": "POST",
                        "path": "/file-attachment-styling",
                        "description": "Get file attachment component styling", 
                        "returns": "CSS and HTML for file upload elements"
                    },
                    "errorMessageStyling": {
                        "method": "POST",
                        "path": "/error-message-styling",
                        "description": "Get error message styling",
                        "returns": "CSS and HTML for form validation errors"
                    },
                    "repeatablePanelStyling": {
                        "method": "POST", 
                        "path": "/repeatable-panel-styling",
                        "description": "Get repeatable panel styling",
                        "returns": "CSS and HTML for dynamic repeatable form sections"
                    },
                    "customComponentCreation": {
                        "method": "POST",
                        "path": "/custom-component-creation",
                        "description": "Get complete documentation for creating custom components (decorating fields)",
                        "returns": "Complete guide with decorator functions, custom styling, and behavior implementation"
                    },
                    "layoutConfiguration": {
                        "method": "POST",
                        "path": "/layout-configuration",
                        "description": "Get complete documentation for panel layout configuration",
                        "returns": "Complete guide for implementing custom layouts like accordion, wizard, tabs, etc."
                    },
                    "systemInfoPost": {
                        "method": "POST",
                        "path": "/system-info",
                        "description": "Get system information (POST endpoint)",
                        "returns": "System details and environment info"
                    }
                },
                "usage": {
                    "baseURL": "http://localhost:8080",
                    "contentType": "application/json",
                    "authentication": "none",
                    "cors": "enabled"
                }
            }

        @app.get("/api/schema")
        async def api_schema():
            """Get OpenAPI-like schema for all endpoints"""
            return {
                "openapi": "3.0.0",
                "info": {
                    "title": "FORMS Edge Delivery MCP Server",
                    "version": "1.0.0",
                    "description": "MCP server providing FORMS styling and structure data for Adobe Experience Manager"
                },
                "servers": [
                    {"url": "http://localhost:8080", "description": "Local development server"}
                ],
                "paths": {
                    "/health": {
                        "get": {
                            "summary": "Health Check",
                            "description": "Check if server is running and healthy",
                            "responses": {
                                "200": {
                                    "description": "Server is healthy",
                                    "content": {
                                        "application/json": {
                                            "schema": {
                                                "type": "object",
                                                "properties": {
                                                    "status": {"type": "string", "example": "healthy"},
                                                    "timestamp": {"type": "string"},
                                                    "server": {"type": "string"}
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "/field-structure": {
                        "post": {
                            "summary": "Get Field Structure Styling",
                            "description": "Returns HTML structure and CSS styling for form fields",
                            "responses": {
                                "200": {
                                    "description": "Field structure data",
                                    "content": {
                                        "application/json": {
                                            "schema": {
                                                "type": "object",
                                                "properties": {
                                                    "status": {"type": "string"},
                                                    "data": {"type": "string"},
                                                    "timestamp": {"type": "string"}
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                "components": {
                    "schemas": {
                        "ApiResponse": {
                            "type": "object",
                            "properties": {
                                "status": {"type": "string", "enum": ["success", "error"]},
                                "data": {"type": "string"},
                                "errorMessage": {"type": "string"},
                                "timestamp": {"type": "string"}
                            }
                        }
                    }
                }
            }
        
        # Run HTTP server
        uvicorn.run(
            app,
            host=SERVER_CONFIG['host'],
            port=SERVER_CONFIG['port'],
            log_level="info" if SERVER_CONFIG['debug'] else "warning"
        )
    else:
        # Default STDIO transport for MCP protocol
        mcp.run()

if __name__ == "__main__":
    main()
