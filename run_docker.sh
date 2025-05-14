#!/bin/bash

echo "🐳 Building Docker image..."
docker build -t house-price-prediction .

echo "🚀 Running Docker container..."
docker run -p 8000:8000 house-price-prediction
