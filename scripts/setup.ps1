# Sutradhar Setup Script for Windows
# This script sets up the development environment

$ErrorActionPreference = "Stop"

Write-Host "Setting up Sutradhar development environment..." -ForegroundColor Green

# Check if Docker is installed
try {
    $dockerVersion = docker --version
    Write-Host "Docker found: $dockerVersion" -ForegroundColor Green
} catch {
    Write-Host "Docker is not installed. Please install Docker Desktop first." -ForegroundColor Red
    exit 1
}

# Check if Docker Compose is installed
try {
    $dockerComposeVersion = docker-compose --version
    Write-Host "Docker Compose found: $dockerComposeVersion" -ForegroundColor Green
} catch {
    Write-Host "Docker Compose is not installed. Please install Docker Compose first." -ForegroundColor Red
    exit 1
}

# Create environment files if they don't exist
if (-not (Test-Path .env)) {
    Write-Host "Creating .env file from .env.example..." -ForegroundColor Yellow
    Copy-Item .env.example .env
}

if (-not (Test-Path backend\.env)) {
    Write-Host "Creating backend\.env file from backend\.env.example..." -ForegroundColor Yellow
    Copy-Item backend\.env.example backend\.env
}

if (-not (Test-Path frontend\.env.local)) {
    Write-Host "Creating frontend\.env.local file from frontend\.env.example..." -ForegroundColor Yellow
    Copy-Item frontend\.env.example frontend\.env.local
}

# Build and start Docker containers
Write-Host "Building Docker containers..." -ForegroundColor Yellow
docker-compose build

Write-Host "Starting Docker containers..." -ForegroundColor Yellow
docker-compose up -d

Write-Host "Waiting for services to be ready..." -ForegroundColor Yellow
Start-Sleep -Seconds 10

# Check if services are running
Write-Host "Checking service status..." -ForegroundColor Yellow
docker-compose ps

Write-Host ""
Write-Host "Setup complete!" -ForegroundColor Green
Write-Host "Frontend: http://localhost:3000" -ForegroundColor Cyan
Write-Host "Backend API: http://localhost:8000" -ForegroundColor Cyan
Write-Host "API Docs: http://localhost:8000/docs" -ForegroundColor Cyan
Write-Host ""
Write-Host "To stop services: docker-compose down" -ForegroundColor Yellow
Write-Host "To view logs: docker-compose logs -f" -ForegroundColor Yellow
