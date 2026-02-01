FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Set environment variable to ensure output is unbuffered
ENV PYTHONUNBUFFERED=1

# Expose the MCP server
CMD ["python3", "-m", "mcp_server.server"]
