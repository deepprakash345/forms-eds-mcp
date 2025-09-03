"""
Shared utilities for FORMS Edge Delivery MCP managers.

Contains common functions used across different component managers.
"""

import requests
import re
import json
from typing import Tuple


def fetch_adobe_docs() -> Tuple[str, str]:
    """
    Helper function to fetch Adobe documentation content.
    
    Returns:
        Tuple[str, str]: (content, url) - The documentation content and source URL
        
    Raises:
        Exception: If documentation cannot be fetched
    """
    DOCS_URL = "https://main--afb--adobe.aem.live/docs/developer/theme.md"
    try:
        response = requests.get(DOCS_URL, timeout=10)
        response.raise_for_status()
        return response.text, DOCS_URL
    except requests.exceptions.RequestException as e:
        raise Exception(f"Unable to fetch documentation: {str(e)}")


def clean_content(content: str) -> str:
    """
    Helper function to clean and format extracted content.
    
    Args:
        content (str): Raw content to clean
        
    Returns:
        str: Cleaned and formatted content
    """
    cleaned = content.replace('\\*\\*', '**').replace('\\`\\`\\`', '```')
    cleaned = cleaned.replace('\\#', '#').replace('\\-', '-')
    cleaned = re.sub(r'\n\s*\n\s*\n', '\n\n', cleaned)
    return cleaned.strip()


def create_success_response(data: str) -> str:
    """
    Create a successful JSON response.
    
    Args:
        data (str): The data to include in the response
        
    Returns:
        str: JSON string response
    """
    return json.dumps({
        "status": "success",
        "data": data,
        "errorMessage": None
    })


def create_error_response(error_message: str) -> str:
    """
    Create an error JSON response.
    
    Args:
        error_message (str): The error message
        
    Returns:
        str: JSON string response
    """
    return json.dumps({
        "status": "failure", 
        "data": None,
        "errorMessage": error_message
    })


def extract_content_patterns(docs_content: str, patterns: list, docs_url: str, title: str) -> str:
    """
    Extract content using regex patterns and create formatted result.
    
    Args:
        docs_content (str): The documentation content to search
        patterns (list): List of regex patterns to match
        docs_url (str): Source URL for attribution
        title (str): Title for the extracted content
        
    Returns:
        str: Extracted and formatted content or None if no content found
    """
    extracted_content = []
    for pattern in patterns:
        matches = re.findall(pattern, docs_content, re.DOTALL | re.IGNORECASE)
        for match in matches:
            if match.strip():
                extracted_content.append(clean_content(match))
    
    if extracted_content:
        result = f"# {title}\n\n"
        result += "\n\n---\n\n".join(extracted_content)
        result += f"\n\n---\n\n*Information from [Adobe Adaptive Form Theme Documentation]({docs_url})*"
        return result
    
    return None
