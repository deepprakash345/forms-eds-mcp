"""
Repeatable Panel Tools for MCP server.

Contains MCP tool wrapper for repeatable panel styling components.
"""

from fastmcp import FastMCP
from ..managers.repeatable_panel_manager import get_repeatable_panel_styling as repeatable_panel_styling_manager


def register_repeatable_panel_tools(mcp: FastMCP):
    """Register repeatable panel tools with the MCP server."""
    
    @mcp.tool
    def get_repeatable_panel_styling() -> str:
        """
        Get repeatable panel component structure for dynamic form sections.
        Covers dynamic panel creation, repetition controls, and container styling.
        
        Returns:
            Repeatable panel implementation with dynamic section controls and styling
        """
        return repeatable_panel_styling_manager()
