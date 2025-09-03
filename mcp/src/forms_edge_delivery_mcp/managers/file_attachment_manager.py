"""
File Attachment Manager for FORMS Edge Delivery MCP server.

Handles file upload component documentation retrieval and fallback content.
"""

from .shared_utils import (
    fetch_adobe_docs, 
    create_success_response, 
    create_error_response,
    extract_content_patterns
)


def get_file_attachment_styling_fallback() -> str:
    """Returns fallback content for file attachment documentation."""
    return """
# File Attachment Styling - No Content Found

The file attachment documentation could not be extracted.

### 🔗 **Direct Access:**
Visit: https://main--afb--adobe.aem.live/docs/developer/theme.md

### 📎 **General Pattern:**
File attachments typically include:
- `.file-wrapper` container class
- Drag and drop area with visual feedback
- Hidden file input element
- File list container for uploaded files
- Upload button and progress indicators
"""


def get_file_attachment_styling() -> str:
    """
    Get file upload component structure with drag-drop functionality.
    Covers file attachment HTML structure, drag-drop areas, and upload styling.
    
    Returns:
        JSON string with file attachment component information
    """
    try:
        docs_content, docs_url = fetch_adobe_docs()
        
        # Extract file attachment patterns
        patterns = [
            r"### \*\*File Attachment\*\*(.*?)(?=##|\Z)"
        ]
        
        extracted_content = extract_content_patterns(
            docs_content, 
            patterns, 
            docs_url, 
            "File Attachment Component"
        )
        
        if extracted_content:
            return create_success_response(extracted_content)
        else:
            return create_success_response(get_file_attachment_styling_fallback())
            
    except Exception as e:
        return create_error_response(f"Error fetching file attachment documentation: {str(e)}")
