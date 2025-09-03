"""
Custom Component Manager for FORMS Edge Delivery MCP server.

Handles custom component creation documentation retrieval and fallback content.
"""

import requests
import json
from typing import Tuple


def fetch_component_docs() -> Tuple[str, str]:
    """
    Helper function to fetch Adobe custom component documentation content.
    
    Returns:
        Tuple[str, str]: (content, url) - The documentation content and source URL
        
    Raises:
        Exception: If documentation cannot be fetched
    """
    DOCS_URL = "https://main--afb--adobe.aem.live/docs/developer/component.md"
    try:
        response = requests.get(DOCS_URL, timeout=10)
        response.raise_for_status()
        return response.text, DOCS_URL
    except requests.exceptions.RequestException as e:
        raise Exception(f"Unable to fetch component documentation: {str(e)}")


def get_custom_component_fallback() -> str:
    """Returns fallback content for custom component documentation."""
    return """
# Create Custom Component (Decorate Field) - No Content Found

The custom component documentation could not be extracted.

### 🔗 **Direct Access:**
Visit: https://main--afb--adobe.aem.live/docs/developer/component.md

### 🎨 **General Pattern:**
Custom components typically involve:
- Creating a decorator function in components folder
- Manipulating the fieldEl (default markup)
- Adding custom behavior and styling
- Preserving accessibility attributes
- Cloning original elements rather than rebuilding from scratch

### 📝 **Basic Structure:**
```javascript
export default function decorate(fieldEl, field) {
    // fieldEl: default markup of form element
    // field: properties defined by author
    // ... code to manipulate fieldEl
    return fieldEl;
}
```
"""


def get_custom_component_creation() -> str:
    """
    Get complete documentation for creating custom components (decorating fields) in Adaptive Form Block.
    Covers the entire process from creation to styling of custom form components.
    
    Returns:
        JSON string with complete custom component creation documentation
    """
    try:
        docs_content, docs_url = fetch_component_docs()
        
        if docs_content and docs_content.strip():
            # Return the entire document content as requested
            result = f"# Create Custom Component (Decorate Field) in Adaptive Form Block\n\n"
            result += docs_content
            result += f"\n\n---\n\n*Complete documentation from [Adobe Custom Component Documentation]({docs_url})*"
            
            return json.dumps({
                "status": "success",
                "data": result,
                "errorMessage": None
            })
        else:
            return json.dumps({
                "status": "success",
                "data": get_custom_component_fallback(),
                "errorMessage": None
            })
            
    except Exception as e:
        return json.dumps({
            "status": "failure",
            "data": None,
            "errorMessage": f"Error fetching custom component documentation: {str(e)}"
        })
