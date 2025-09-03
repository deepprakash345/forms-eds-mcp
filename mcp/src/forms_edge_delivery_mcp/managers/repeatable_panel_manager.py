"""
Repeatable Panel Manager for FORMS Edge Delivery MCP server.

Handles repeatable panel component documentation retrieval and fallback content.
"""

from .shared_utils import (
    fetch_adobe_docs, 
    create_success_response, 
    create_error_response,
    extract_content_patterns
)


def get_repeatable_panel_styling_fallback() -> str:
    """Returns fallback content for repeatable panel documentation."""
    return """
# Repeatable Panel Styling - No Content Found

The repeatable panel documentation could not be extracted.

### 🔗 **Direct Access:**
Visit: https://main--afb--adobe.aem.live/docs/developer/theme.md

### 🔄 **General Pattern:**
Repeatable panels typically include:
- Panel container with repeatable property
- Add/Remove buttons for dynamic control
- Instance numbering or indexing
- Consistent styling across instances
- JavaScript controls for dynamic behavior
"""


def get_repeatable_panel_styling() -> str:
    """
    Get repeatable panel component structure for dynamic form sections.
    Covers dynamic panel creation, repetition controls, and container styling.
    
    Returns:
        JSON string with repeatable panel component information
    """
    try:
        docs_content, docs_url = fetch_adobe_docs()
        
        # Extract repeatable panel patterns
        patterns = [
            r"## Repeatable Panel(.*?)(?=##|\Z)"
        ]
        
        extracted_content = extract_content_patterns(
            docs_content, 
            patterns, 
            docs_url, 
            "Repeatable Panel Component"
        )
        
        if extracted_content:
            return create_success_response(extracted_content)
        else:
            return create_success_response(get_repeatable_panel_styling_fallback())
            
    except Exception as e:
        return create_error_response(f"Error fetching repeatable panel documentation: {str(e)}")
