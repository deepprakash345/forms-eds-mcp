"""
File Attachment Tools for MCP server.

Contains MCP tool wrapper for file attachment styling components.
"""

from fastmcp import FastMCP
from ..managers.file_attachment_manager import get_file_attachment_styling as file_attachment_styling_manager


def register_file_attachment_tools(mcp: FastMCP):
    """Register file attachment tools with the MCP server."""
    
    @mcp.tool
    def get_file_attachment_styling() -> str:
        """
        Get file upload component structure with drag-drop functionality.
        Covers file attachment HTML structure, drag-drop areas, and upload styling.
        
        Returns:
            Complete file attachment component with drag-drop implementation and styling
        """
        return file_attachment_styling_manager()
