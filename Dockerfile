# Start from official Python slim image
# Slim means minimal base image - smaller attack surface
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Create a non-root user for security
# Running as root inside containers is a security risk
RUN useradd -m -u 1000 appuser

# Copy application code into the container
COPY app.py .

# Change ownership to the non-root user
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Document which port the app listens on
EXPOSE 8080

# Set environment variables
ENV APP_ENV=production
ENV PORT=8080

# Health check so Kubernetes knows if the container is healthy
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python3 -c "import urllib.request; urllib.request.urlopen('http://localhost:8080')"

# Command to run when container starts
CMD ["python3", "app.py"]