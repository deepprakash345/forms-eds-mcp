"""
CSS Selectors Manager for FORMS Edge Delivery MCP server.

Handles CSS selectors and targeting techniques documentation retrieval and fallback content.
"""

from .shared_utils import (
    fetch_adobe_docs, 
    create_success_response, 
    create_error_response,
    extract_content_patterns
)


def get_css_selectors_guide_fallback() -> str:
    """Returns fallback content for CSS selectors documentation."""
    return """
# CSS Selectors Guide - No Content Found

The CSS selectors documentation could not be extracted.

### 🔗 **Direct Access:**
Visit: https://main--afb--adobe.aem.live/docs/developer/theme.md

### 🎨 **Common Patterns:**
- `.{type}-wrapper` - Target by field type (e.g., `.text-wrapper`)
- `.field-{name}` - Target by field name (e.g., `.field-email`)
- `[data-required="true"]` - Target required fields
- `.field-invalid` - Target invalid/error fields
"""


def get_css_selectors_guide() -> str:
    """
    Get CSS selectors and targeting techniques for styling form fields.
    Covers type-based selectors, name-based targeting, and advanced styling patterns.
    
    Returns:
        JSON string with CSS selectors guide information
    """
    try:
        docs_content, docs_url = fetch_adobe_docs()
        
        # Extract styling/selectors patterns
        patterns = [
            r"## \*\*Styling Fields\*\*(.*?)(?=###|\Z)",
            r"### \*\*Styling based on Field Type\.\*\*(.*?)(?=###|\Z)",
            r"### \*\*Styling specific field type\.\*\*(.*?)(?=###|\Z)"
        ]
        
        extracted_content = extract_content_patterns(
            docs_content, 
            patterns, 
            docs_url, 
            "CSS Selectors & Styling Techniques"
        )
        
        if extracted_content:
            return create_success_response(extracted_content)
        else:
            return create_success_response(get_css_selectors_guide_fallback())
            
    except Exception as e:
        return create_error_response(f"Error fetching CSS selectors documentation: {str(e)}")
