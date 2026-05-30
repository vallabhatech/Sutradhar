#!/bin/bash

# Development script to start services in development mode with hot reload

set -e

echo "Starting Sutradhar in development mode..."

# Start services with hot reload enabled
docker-compose up

# To run in background:
# docker-compose up -d
