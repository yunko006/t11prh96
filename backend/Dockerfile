# Production Dockerfile for FastAPI backend
FROM python:3.12-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Copy workspace configuration files
COPY pyproject.toml uv.lock /app/

# Copy backend package
COPY backend /app/backend

# Sync dependencies from lock file (production only, no dev dependencies)
RUN uv sync --frozen --no-dev

# Create non-root user for security
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health').read()" || exit 1

# Run FastAPI application in production mode
CMD ["uv", "run", "fastapi", "run", "backend/main.py", "--host", "0.0.0.0", "--port", "8000"]
