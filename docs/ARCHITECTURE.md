# Architecture

## Overview

Sutradhar follows a clean architecture pattern with clear separation of concerns across frontend, backend, and infrastructure layers.

## Backend Architecture

### Layer Structure

```
backend/
├── app/
│   ├── api/          # API endpoints and routing
│   ├── core/         # Configuration and settings
│   ├── models/       # SQLAlchemy database models
│   ├── schemas/      # Pydantic schemas for validation
│   ├── services/     # Business logic layer
│   ├── repositories/ # Data access layer
│   ├── database/     # Database session management
│   ├── middleware/   # Custom middleware
│   └── main.py       # Application entry point
└── tests/            # Test suite
```

### Design Principles

- **Dependency Injection**: Database sessions and dependencies injected via FastAPI's dependency system
- **Async/Await**: All database operations use async patterns for better performance
- **Type Safety**: Strong typing with Pydantic and mypy
- **Separation of Concerns**: Clear boundaries between API, business logic, and data access layers

## Frontend Architecture

### Layer Structure

```
frontend/
├── src/
│   ├── app/          # Next.js app router pages
│   ├── components/   # Reusable React components
│   ├── services/     # API client services
│   ├── hooks/        # Custom React hooks
│   ├── lib/          # Utility functions
│   ├── types/        # TypeScript type definitions
│   └── styles/       # Global styles
└── public/           # Static assets
```

### Design Principles

- **Component-Based**: Modular, reusable React components
- **Type Safety**: Full TypeScript coverage
- **Server-Side Rendering**: Next.js App Router for optimal performance
- **Styling**: Tailwind CSS for utility-first styling

## Infrastructure

### Docker Services

- **PostgreSQL**: Primary database with persistent volume
- **FastAPI Backend**: Async Python API server
- **Next.js Frontend**: React-based web application
- **Nginx**: Reverse proxy (optional, for production routing)

### Network Architecture

All services communicate via a dedicated Docker bridge network for security and isolation.

## Data Flow

1. **Frontend** makes API calls to **Backend** via HTTP/REST
2. **Backend** processes requests through **Services** layer
3. **Services** interact with **Repositories** for data access
4. **Repositories** use **Database** session for PostgreSQL operations
5. **Responses** flow back through the same layers

## Security Considerations

- Environment-based configuration
- CORS configuration for cross-origin requests
- Secret key management via environment variables
- Database credentials not hardcoded
- Container isolation via Docker

## Scalability

The architecture supports horizontal scaling:
- Stateless backend services
- Database connection pooling
- Load balancer ready (via Nginx)
- Container orchestration ready (Docker Compose → Kubernetes)
