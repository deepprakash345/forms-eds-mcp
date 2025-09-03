"""
Layout Manager for FORMS Edge Delivery MCP server.

Handles panel layout configuration documentation retrieval and fallback content.
"""

import requests
import json
from typing import Tuple


def fetch_layout_docs() -> Tuple[str, str]:
    """
    Helper function to fetch Adobe layout configuration documentation content.
    
    Returns:
        Tuple[str, str]: (content, url) - The documentation content and source URL
        
    Raises:
        Exception: If documentation cannot be fetched
    """
    DOCS_URL = "https://main--afb--adobe.aem.live/docs/developer/layout.md"
    try:
        response = requests.get(DOCS_URL, timeout=10)
        response.raise_for_status()
        return response.text, DOCS_URL
    except requests.exceptions.RequestException as e:
        raise Exception(f"Unable to fetch layout documentation: {str(e)}")


def get_layout_configuration_fallback() -> str:
    """Returns fallback content for layout configuration documentation."""
    return """
# Custom Layout Configuration - No Content Found

The layout configuration documentation could not be extracted.

### 🔗 **Direct Access:**
Visit: https://main--afb--adobe.aem.live/docs/developer/layout.md

### 🎨 **General Pattern:**
Layout configuration typically involves:
- Opening the mappings.js file and locating the componentDecorator function
- Adding new conditions based on the :type property
- Creating new JavaScript files inside the "components" folder
- Implementing layout-specific functionality (accordion, wizard, tabs, etc.)
- Applying appropriate CSS classes for styling

### 📝 **Basic Structure:**
```javascript
export default async function componentDecorator(fd) {
    const { ':type': type = '', fieldType } = fd;
    
    if (type.endsWith('accordion')) {
        const module = await import('./components/accordion.js');
        return module.default;
    }
    
    // Add more layout conditions
    return null;
}
```

### 🏗️ **Layout Implementation:**
```javascript
export class AccordionLayout {
    applyLayout(panel) {
        panel.classList.add('accordion');
        // Implement accordion functionality
    }
}

const layout = new AccordionLayout();
export default function accordionLayout(panel) {
    layout.applyLayout(panel);
}
```
"""


def get_layout_configuration() -> str:
    """
    Get complete documentation for panel layout configuration in Adaptive Form Block.
    Covers the entire process from componentDecorator function to layout implementation.
    
    Returns:
        JSON string with complete layout configuration documentation
    """
    try:
        docs_content, docs_url = fetch_layout_docs()
        
        if docs_content and docs_content.strip():
            # Return the entire document content as requested
            result = f"# Custom Layout Configuration for Panel\n\n"
            result += docs_content
            result += f"\n\n---\n\n*Complete documentation from [Adobe Layout Configuration Documentation]({docs_url})*"
            
            return json.dumps({
                "status": "success",
                "data": result,
                "errorMessage": None
            })
        else:
            return json.dumps({
                "status": "success",
                "data": get_layout_configuration_fallback(),
                "errorMessage": None
            })
            
    except Exception as e:
        return json.dumps({
            "status": "failure",
            "data": None,
            "errorMessage": f"Error fetching layout configuration documentation: {str(e)}"
        })
