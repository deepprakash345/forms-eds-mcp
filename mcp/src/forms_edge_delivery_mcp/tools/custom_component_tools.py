"""
Custom Component Tools for MCP server.

Contains MCP tool wrapper for custom component creation documentation.
"""

from fastmcp import FastMCP
from ..managers.custom_component_manager import get_custom_component_creation as custom_component_manager


def register_custom_component_tools(mcp: FastMCP):
    """Register custom component tools with the MCP server."""
    
    @mcp.tool
    def get_custom_component_creation() -> str:
        """
        Get complete documentation for creating custom components (decorating fields) in Adaptive Form Block.
        Covers the entire process from decorator functions to custom styling and behavior implementation.
        
        Returns:
            Complete custom component creation guide with code examples and styling techniques
        """
        return custom_component_manager()
