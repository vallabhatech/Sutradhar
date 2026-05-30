#!/bin/bash

# Test script to run backend tests

set -e

echo "Running backend tests..."

# Run tests in backend container
docker-compose exec backend pytest -v

echo "Tests completed!"
