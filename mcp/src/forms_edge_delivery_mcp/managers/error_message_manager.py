"""
Error Message Manager for FORMS Edge Delivery MCP server.

Handles form validation and error message documentation retrieval and fallback content.
"""

from .shared_utils import (
    fetch_adobe_docs, 
    create_success_response, 
    create_error_response,
    extract_content_patterns
)


def get_error_message_styling_fallback() -> str:
    """Returns fallback content for error message documentation."""
    return """
# Error Message Styling - No Content Found

The error message documentation could not be extracted.

### 🔗 **Direct Access:**
Visit: https://main--afb--adobe.aem.live/docs/developer/theme.md

### ❌ **General Pattern:**
Error styling typically includes:
- `.field-invalid` class on field wrappers
- `.field-description` for error messages
- Red color schemes for error states
- ARIA attributes for accessibility
- Error icons and visual indicators
"""


def get_error_message_styling() -> str:
    """
    Get form validation and error message styling techniques.
    Covers error states, validation feedback, and error message presentation.
    
    Returns:
        JSON string with error message styling information
    """
    try:
        docs_content, docs_url = fetch_adobe_docs()
        
        # Extract error message patterns
        patterns = [
            r"## \*\*Styling Error Messages\*\*(.*?)(?=\+---|$)",
            r"### Error Structure(.*?)(?=###|\Z)",
            r"### Styling error message(.*?)(?=\+---|$)"
        ]
        
        extracted_content = extract_content_patterns(
            docs_content, 
            patterns, 
            docs_url, 
            "Error Message Styling"
        )
        
        if extracted_content:
            return create_success_response(extracted_content)
        else:
            return create_success_response(get_error_message_styling_fallback())
            
    except Exception as e:
        return create_error_response(f"Error fetching error message documentation: {str(e)}")
