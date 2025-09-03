"""
Radio & Checkbox Tools for MCP server.

Contains MCP tool wrapper for radio button and checkbox styling components.
"""

from fastmcp import FastMCP
from ..managers.radio_checkbox_manager import get_radio_checkbox_styling as radio_checkbox_styling_manager


def register_radio_checkbox_tools(mcp: FastMCP):
    """Register radio and checkbox tools with the MCP server."""
    
    @mcp.tool
    def get_radio_checkbox_styling() -> str:
        """
        Get radio button and checkbox group component structures and styling.
        Covers fieldset implementation, group organization, and styling techniques.
        
        Returns:
            Complete radio and checkbox group implementation with HTML structures and CSS
        """
        return radio_checkbox_styling_manager()
