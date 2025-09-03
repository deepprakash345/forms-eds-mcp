"""
Panel & Container Tools for MCP server.

Contains MCP tool wrapper for panel and container styling components.
"""

from fastmcp import FastMCP
from ..managers.panel_container_manager import get_panel_container_styling as panel_container_styling_manager


def register_panel_container_tools(mcp: FastMCP):
    """Register panel and container tools with the MCP server."""
    
    @mcp.tool
    def get_panel_container_styling() -> str:
        """
        Get panel and container component structures for grouping form elements.
        Covers fieldset implementation, panel organization, and container styling.
        
        Returns:
            Panel and container implementation with HTML structure and styling techniques
        """
        return panel_container_styling_manager()
