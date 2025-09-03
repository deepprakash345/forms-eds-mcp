"""
Field Structure Manager for FORMS Edge Delivery MCP server.

Handles field structure documentation retrieval and fallback content.
"""

from .shared_utils import (
    fetch_adobe_docs, 
    create_success_response, 
    create_error_response,
    extract_content_patterns
)


def get_field_structure_fallback() -> str:
    """Returns fallback content for field structure documentation."""
    return """
# Field Structure - No Content Found

The field structure documentation could not be extracted. 

### 🔗 **Direct Access:**
Visit: https://main--afb--adobe.aem.live/docs/developer/theme.md

### 🏗️ **General Pattern:**
Adaptive Form fields typically follow this structure:
- Wrapper div with type and name classes
- Label element with proper association  
- Input/select element with attributes
- Description div for hints/help text
"""


def get_field_structure_styling() -> str:
    """
    Get HTML structure and markup patterns for Adaptive Form fields.
    Covers general field structure for text, number, email, and other input types.
    
    Returns:
        JSON string with field structure information
    """
    try:
        docs_content, docs_url = fetch_adobe_docs()
        
        # Extract field structure patterns
        patterns = [
            r"## \*\*Field Structure\*\*(.*?)(?=###|\Z)",
            r"Every Form Field.*?follows below structure(.*?)(?=- \*\*Type\*\*|\Z)"
        ]
        
        extracted_content = extract_content_patterns(
            docs_content, 
            patterns, 
            docs_url, 
            "Adaptive Form Field Structure"
        )
        
        if extracted_content:
            return create_success_response(extracted_content)
        else:
            return create_success_response(get_field_structure_fallback())
            
    except Exception as e:
        return create_error_response(f"Error fetching field structure documentation: {str(e)}")
