"""
System Info Manager for FORMS Edge Delivery MCP server.

Handles system information retrieval and formatting.
"""

import json
from ..resources.system import get_system_info


def get_system_information() -> str:
    """
    Get system information including platform, Python version, and environment details.
    
    Returns:
        JSON string with system information
    """
    try:
        info = get_system_info()
        
        result = "🖥️ System Information:\n\n"
        
        # Platform info
        platform_info = info['platform']
        result += f"🔧 Platform: {platform_info['system']} {platform_info['release']}\n"
        result += f"🏗️ Architecture: {platform_info['machine']}\n"
        
        # Python info  
        python_info = info['python']
        result += f"🐍 Python: {python_info['version_info']['major']}.{python_info['version_info']['minor']}.{python_info['version_info']['micro']}\n"
        
        # Environment
        env_info = info['environment']
        result += f"📁 Working Directory: {env_info['working_directory']}\n"
        result += f"👤 User: {env_info['user']}\n"
        
        result += f"\n🕐 Timestamp: {info['timestamp']}\n"
        
        return json.dumps({
            "status": "success",
            "data": result,
            "errorMessage": None
        })
    except Exception as e:
        return json.dumps({
            "status": "failure",
            "data": None,
            "errorMessage": f"Error getting system info: {str(e)}"
        })
