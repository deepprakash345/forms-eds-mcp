# Use Ubuntu as base image
FROM ubuntu:22.04

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV MCP_PORT=8080
ENV MCP_HOST=0.0.0.0
ENV MCP_DEBUG=false

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    curl \
    wget \
    git \
    && rm -rf /var/lib/apt/lists/*

# Create and activate virtual environment
RUN python3 -m venv /opt/venv
#activate the virtual environment
# No need to activate the virtual environment here; use ENV PATH instead

ENV PATH="/opt/venv/bin:$PATH"

# Upgrade pip
RUN pip install --upgrade pip

# Copy application code first (needed for package installation)
COPY . .

# Install Python dependencies from pyproject.toml (now that source code is available)
RUN pip install -e .

# Create non-root user for security
RUN useradd -m -u 1000 mcpuser && \
    chown -R mcpuser:mcpuser /app /opt/venv
USER mcpuser

# Expose the port
EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:8080/health || exit 1

# Command to run the application
CMD ["python3", "-m", "debugpy", "--listen", "0.0.0.0:5678", "server.py"] 

