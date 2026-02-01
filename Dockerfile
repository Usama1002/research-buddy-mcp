FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Set environment variable to ensure output is unbuffered
ENV PYTHONUNBUFFERED=1

# Expose the MCP server
EXPOSE 8000
CMD ["fastmcp", "run", "mcp_server.server:mcp", "--transport", "sse", "--host", "0.0.0.0", "--port", "8000"]
