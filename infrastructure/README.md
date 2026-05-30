# Infrastructure

This directory contains infrastructure configurations for the Sutradhar platform.

## Docker Configurations

### PostgreSQL
- `docker/postgres/init.sql` - Database initialization script

### Nginx
- `docker/nginx/nginx.conf` - Reverse proxy configuration for routing traffic between frontend and backend

## Usage

The main docker-compose.yml file at the project root orchestrates all services including those defined here.
