"""
Configuration settings for the MCP Server
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SERVER_CONFIG = {
    "name": "FORMS EDGE DELIVERY MCP",
    "version": "1.0.0",
    "description": "FORMS Edge Delivery MCP server providing tools and services for edge delivery operations",
    "transport": os.getenv("MCP_TRANSPORT", "stdio"),  # Options: "stdio", "http"
    "port": int(os.getenv("MCP_PORT", 8000)),
    "host": os.getenv("MCP_HOST", "localhost"),
    "allowed_origins": ["*"],  # CORS settings for HTTP transport
    "debug": os.getenv("MCP_DEBUG", "false").lower() == "true"
}

# External API configurations
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "")  # Add your weather API key here
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"

# File operation settings
ALLOWED_FILE_EXTENSIONS = {".txt", ".json", ".csv", ".md", ".py", ".js", ".html", ".css"}
MAX_FILE_SIZE_MB = 10
