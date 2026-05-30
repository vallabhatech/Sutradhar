# Scripts

This directory contains utility scripts for development and deployment.

## Setup Scripts

### setup.sh (Linux/Mac)
Initial setup script for Linux and Mac systems.

**Usage:**
```bash
chmod +x scripts/setup.sh
./scripts/setup.sh
```

### setup.ps1 (Windows)
Initial setup script for Windows systems.

**Usage:**
```powershell
.\scripts\setup.ps1
```

**What it does:**
- Checks for Docker and Docker Compose installation
- Creates environment files from examples
- Builds Docker containers
- Starts all services
- Displays service status

## Development Scripts

### dev.sh (Linux/Mac)
Start all services in development mode with hot reload.

**Usage:**
```bash
chmod +x scripts/dev.sh
./scripts/dev.sh
```

### dev.ps1 (Windows)
Start all services in development mode with hot reload.

**Usage:**
```powershell
.\scripts\dev.ps1
```

## Test Scripts

### test.sh (Linux/Mac)
Run backend tests.

**Usage:**
```bash
chmod +x scripts/test.sh
./scripts/test.sh
```

### test.ps1 (Windows)
Run backend tests.

**Usage:**
```powershell
.\scripts\test.ps1
```

## Making Scripts Executable (Linux/Mac)

Before running shell scripts on Linux or Mac, make them executable:

```bash
chmod +x scripts/*.sh
```

## Common Docker Commands

```bash
# Start all services
docker-compose up -d

# Stop all services
docker-compose down

# View logs
docker-compose logs -f

# Restart a specific service
docker-compose restart backend

# Rebuild a service
docker-compose build backend
docker-compose up -d backend

# Execute commands in a container
docker-compose exec backend bash
docker-compose exec frontend sh
```
