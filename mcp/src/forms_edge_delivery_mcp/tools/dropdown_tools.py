"""
Dropdown Tools for MCP server.

Contains MCP tool wrapper for dropdown styling components.
"""

from fastmcp import FastMCP
from ..managers.dropdown_manager import get_dropdown_styling as dropdown_styling_manager


def register_dropdown_tools(mcp: FastMCP):
    """Register dropdown tools with the MCP server."""
    
    @mcp.tool  
    def get_dropdown_styling() -> str:
        """
        Get dropdown/select component structure and styling information.
        Covers HTML structure, CSS selectors, and styling techniques for dropdown components.
        
        Returns:
            Complete dropdown component implementation with HTML and CSS examples
        """
        return dropdown_styling_manager()
