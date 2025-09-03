"""
System Info Tools for MCP server.

Contains MCP tool wrappers for system information functionality.
"""

from fastmcp import FastMCP
from ..managers.system_info_manager import get_system_information


def register_system_info_tools(mcp: FastMCP):
    """Register system info tools with the MCP server."""
    
    @mcp.tool
    def system_info() -> str:
        """
        Get system information including platform, Python version, and environment details.
        
        Returns:
            JSON formatted system information
        """
        return get_system_information()


# Direct function access for HTTP endpoints (without MCP decoration)
def get_system_info_http():
    """HTTP endpoint wrapper for system information."""
    return get_system_information()
