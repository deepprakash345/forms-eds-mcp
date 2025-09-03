"""
CSS Selectors Tools for MCP server.

Contains MCP tool wrapper for CSS selectors and targeting techniques.
"""

from fastmcp import FastMCP
from ..managers.css_selectors_manager import get_css_selectors_guide as css_selectors_guide_manager


def register_css_selectors_tools(mcp: FastMCP):
    """Register CSS selectors tools with the MCP server."""
    
    @mcp.tool
    def get_css_selectors_guide() -> str:
        """
        Get CSS selectors and targeting techniques for styling form fields.
        Covers type-based selectors, name-based targeting, and advanced styling patterns.
        
        Returns:
            Comprehensive guide to CSS selectors with examples for different targeting strategies
        """
        return css_selectors_guide_manager()
