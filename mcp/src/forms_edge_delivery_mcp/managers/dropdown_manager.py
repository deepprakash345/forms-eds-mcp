"""
Dropdown Manager for FORMS Edge Delivery MCP server.

Handles dropdown/select component documentation retrieval and fallback content.
"""

from .shared_utils import (
    fetch_adobe_docs, 
    create_success_response, 
    create_error_response,
    extract_content_patterns
)


def get_dropdown_styling_fallback() -> str:
    """Returns fallback content for dropdown styling documentation."""
    return """
# Dropdown Styling - No Content Found

The dropdown documentation could not be extracted.

### 🔗 **Direct Access:**
Visit: https://main--afb--adobe.aem.live/docs/developer/theme.md

### 📝 **General Pattern:**
Dropdowns typically use:
- `.select-wrapper` class for container
- `<select>` element instead of `<input>`
- Option elements for choices
- Same label and description pattern as other fields
"""


def get_dropdown_styling() -> str:
    """
    Get dropdown/select component structure and styling information.
    Covers HTML structure, CSS selectors, and styling techniques for dropdown components.
    
    Returns:
        JSON string with dropdown component information
    """
    try:
        docs_content, docs_url = fetch_adobe_docs()
        
        # Extract dropdown-specific patterns
        patterns = [
            r"### \*\*Dropdown\*\*(.*?)(?=###|\Z)"
        ]
        
        extracted_content = extract_content_patterns(
            docs_content, 
            patterns, 
            docs_url, 
            "Dropdown Component Styling"
        )
        
        if extracted_content:
            return create_success_response(extracted_content)
        else:
            return create_success_response(get_dropdown_styling_fallback())
            
    except Exception as e:
        return create_error_response(f"Error fetching dropdown documentation: {str(e)}")
