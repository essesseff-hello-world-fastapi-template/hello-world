# Use official Python runtime as base image
FROM python:3.14-slim

# Set working directory
WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN uv pip install --system --no-cache -r requirements.txt

# Copy application files
COPY . .

# Expose port 8080
EXPOSE 8080

# Set environment variables
ENV PORT=8080

# Run the application with uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080", "--workers", "2", "--timeout-keep-alive", "60"]
