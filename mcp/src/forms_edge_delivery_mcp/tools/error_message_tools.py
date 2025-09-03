"""
Error Message Tools for MCP server.

Contains MCP tool wrapper for error message styling components.
"""

from fastmcp import FastMCP
from ..managers.error_message_manager import get_error_message_styling as error_message_styling_manager


def register_error_message_tools(mcp: FastMCP):
    """Register error message tools with the MCP server."""
    
    @mcp.tool
    def get_error_message_styling() -> str:
        """
        Get form validation and error message styling techniques.
        Covers error states, validation feedback, and error message presentation.
        
        Returns:
            Complete error handling implementation with validation styling and error states
        """
        return error_message_styling_manager()
