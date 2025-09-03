"""
Layout Tools for MCP server.

Contains MCP tool wrapper for panel layout configuration documentation.
"""

from fastmcp import FastMCP
from ..managers.layout_manager import get_layout_configuration as layout_manager


def register_layout_tools(mcp: FastMCP):
    """Register layout tools with the MCP server."""
    
    @mcp.tool
    def get_layout_configuration() -> str:
        """
        Get complete documentation for panel layout configuration in Adaptive Form Block.
        Covers the entire process from componentDecorator function to layout implementation.
        Includes examples for accordion, wizard, tabs, and other panel layout types.
        
        Returns:
            Complete layout configuration guide with code examples and implementation patterns
        """
        return layout_manager()
