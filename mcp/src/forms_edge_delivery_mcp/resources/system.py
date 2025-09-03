"""
System resources for providing server and system information
"""
import os
import sys
import platform
from datetime import datetime, timezone
from typing import Dict, Any
from ..config import SERVER_CONFIG

def get_server_info() -> Dict[str, Any]:
    """
    Get information about the MCP server
    """
    return {
        "name": SERVER_CONFIG["name"],  
        "version": SERVER_CONFIG["version"],
        "description": SERVER_CONFIG["description"],
        "transport": SERVER_CONFIG["transport"],
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "uptime_info": "Server is running",
        "available_tools": [
            "get_field_structure",
            "get_dropdown_styling",
            "get_radio_checkbox_styling", 
            "get_panel_container_styling",
            "get_css_selectors_guide",
            "get_file_attachment_styling",
            "get_error_message_styling",
            "get_repeatable_panel_styling",
            "get_custom_component_creation",
            "get_layout_configuration",
            "system_info",
            "get_all_prompts"
        ],
        "available_resources": [
            "server-info",
            "system-info"
        ]
    }

def get_system_info() -> Dict[str, Any]:
    """
    Get system information
    """
    return {
        "platform": {
            "system": platform.system(),
            "release": platform.release(),
            "version": platform.version(),
            "machine": platform.machine(),
            "processor": platform.processor(),
            "architecture": platform.architecture()
        },
        "python": {
            "version": sys.version,
            "version_info": {
                "major": sys.version_info.major,
                "minor": sys.version_info.minor,
                "micro": sys.version_info.micro
            },
            "executable": sys.executable,
            "path": sys.path[:3]  # Show first 3 paths only
        },
        "environment": {
            "working_directory": os.getcwd(),
            "user": os.getenv("USER", "unknown"),
            "home": os.getenv("HOME", "unknown"),
            "path": os.getenv("PATH", "")[:200] + "..." if len(os.getenv("PATH", "")) > 200 else os.getenv("PATH", "")
        },
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
