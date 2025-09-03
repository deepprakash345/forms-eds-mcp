"""
FORMS Edge Delivery MCP Package

This package provides tools and services for Adobe Experience Manager FORMS Edge Delivery operations.
It includes managers, tools, prompts, and resources for form styling and structure.
"""

__version__ = "1.0.0"
__author__ = "Deep Prakash Dewanjo"
__email__ = "ddewanji@adobe.com"

# Import main components for easier access
from .server import main
from .config import SERVER_CONFIG

__all__ = ["main", "SERVER_CONFIG", "__version__", "__author__", "__email__"]
