"""
Panel & Container Manager for FORMS Edge Delivery MCP server.

Handles panel and container component documentation retrieval and fallback content.
"""

from .shared_utils import (
    fetch_adobe_docs, 
    create_success_response, 
    create_error_response,
    extract_content_patterns
)


def get_panel_container_styling_fallback() -> str:
    """Returns fallback content for panel/container documentation."""
    return """
# Panel & Container Styling - No Content Found

The panel/container documentation could not be extracted.

### 🔗 **Direct Access:**
Visit: https://main--afb--adobe.aem.live/docs/developer/theme.md

### 📦 **General Pattern:**
Panels typically use:
- `<fieldset>` elements for grouping
- `<legend>` for panel labels/titles
- Panel name classes for targeting
- Nested form elements within the container
"""


def get_panel_container_styling() -> str:
    """
    Get panel and container component structures for grouping form elements.
    Covers fieldset implementation, panel organization, and container styling.
    
    Returns:
        JSON string with panel and container information
    """
    try:
        docs_content, docs_url = fetch_adobe_docs()
        
        # Extract panel/container patterns
        patterns = [
            r"## \*\*Panel/Container Structure\*\*(.*?)(?=##|\Z)"
        ]
        
        extracted_content = extract_content_patterns(
            docs_content, 
            patterns, 
            docs_url, 
            "Panel & Container Components"
        )
        
        if extracted_content:
            return create_success_response(extracted_content)
        else:
            return create_success_response(get_panel_container_styling_fallback())
            
    except Exception as e:
        return create_error_response(f"Error fetching panel/container documentation: {str(e)}")
