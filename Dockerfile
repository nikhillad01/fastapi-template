FROM python:3.11-alpine

# Set work directory
WORKDIR /code

# Install system dependencies in one layer
RUN apk update && apk add --no-cache \
    bash \
    build-base \
    curl \
    libc-dev \
    g++ \
    gnupg \
    krb5 \
    krb5-dev \
    unixodbc-dev \
    libexpat \
    gcc \
    python3-dev \
    musl-dev \
    linux-headers \
    libpq-dev \
    libffi-dev

# Install Python dependencies
COPY ./requirements.txt .
RUN pip install --upgrade pip setuptools==75.1.0 && \
    pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY ./app /code/app

# Create non-root user
RUN adduser -u 997 -D app && chown -R app:app /code

# Switch to non-root user
USER 997

# Expose port (for uvicorn)
EXPOSE 8000

# Run app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
