# Use the official Python image as the base
FROM nvidia/cuda:12.0.0-devel-ubuntu22.04

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set environment variables for uv
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

# Set the working directory
WORKDIR /app

# # Copy the FastAPI application code
COPY ./app /app/app

RUN echo "Contents of /app after copying app:" && ls -lah /app

# Copy pyproject.toml and uv.lock for dependency management
COPY pyproject.toml uv.lock ./

# Install the application dependencies
RUN uv pip install --system torch torchvision setuptools wheel
RUN uv pip install --system flash-attn --no-build-isolation 

RUN echo "Contents of /app after copying app:" && ls -lah 
RUN uv pip install --system .

# Expose the backend port
EXPOSE 8000

ENV PYTHONPATH="/app/app"

# Command to run the backend using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
