"""
Field Structure Tools for MCP server.

Contains MCP tool wrapper for field structure styling components.
"""

from fastmcp import FastMCP
from ..managers.field_structure_manager import get_field_structure_styling


def register_field_structure_tools(mcp: FastMCP):
    """Register field structure tools with the MCP server."""
    
    @mcp.tool
    def get_field_structure() -> str:
        """
        Get HTML structure and markup patterns for Adaptive Form fields.
        Covers general field structure for text, number, email, and other input types.
        
        Returns:
            Detailed HTML structure with classes, attributes, and field organization patterns
        """
        return get_field_structure_styling()
