# Development script to start services in development mode with hot reload

Write-Host "Starting Sutradhar in development mode..." -ForegroundColor Green

# Start services with hot reload enabled
docker-compose up

# To run in background:
# docker-compose up -d
