"""
Radio & Checkbox Manager for FORMS Edge Delivery MCP server.

Handles radio button and checkbox group documentation retrieval and fallback content.
"""

from .shared_utils import (
    fetch_adobe_docs, 
    create_success_response, 
    create_error_response,
    extract_content_patterns
)


def get_radio_checkbox_styling_fallback() -> str:
    """Returns fallback content for radio/checkbox group documentation."""
    return """
# Radio & Checkbox Groups - No Content Found

The radio/checkbox group documentation could not be extracted.

### 🔗 **Direct Access:**
Visit: https://main--afb--adobe.aem.live/docs/developer/theme.md

### 🔘 **General Pattern:**
Radio/Checkbox groups typically use:
- `<fieldset>` container with legend
- `.radio-wrapper` or `.checkbox-wrapper` classes
- Individual `.field-item` containers for each option
- Unique IDs for each radio/checkbox input
"""


def get_radio_checkbox_styling() -> str:
    """
    Get radio button and checkbox group component structures and styling.
    Covers fieldset implementation, group organization, and styling techniques.
    
    Returns:
        JSON string with radio and checkbox group information
    """
    try:
        docs_content, docs_url = fetch_adobe_docs()
        
        # Extract radio and checkbox patterns
        patterns = [
            r"### \*\*Radio Group\*\*(.*?)(?=###|\Z)",
            r"### \*\*Checkbox Group\*\*(.*?)(?=###|\Z)"
        ]
        
        extracted_content = extract_content_patterns(
            docs_content, 
            patterns, 
            docs_url, 
            "Radio & Checkbox Group Components"
        )
        
        if extracted_content:
            return create_success_response(extracted_content)
        else:
            return create_success_response(get_radio_checkbox_styling_fallback())
            
    except Exception as e:
        return create_error_response(f"Error fetching radio/checkbox documentation: {str(e)}")
