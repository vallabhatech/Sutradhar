# Development Guide

## Prerequisites

- Docker and Docker Compose
- Python 3.12+ (for local backend development)
- Node.js 20+ (for local frontend development)
- PostgreSQL 16+ (if running locally without Docker)

## Local Development Setup

### Backend Development

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Run the server:**
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

6. **Run tests:**
   ```bash
   pytest
   ```

### Frontend Development

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Set environment variables:**
   ```bash
   cp .env.example .env.local
   # Edit .env.local with your configuration
   ```

4. **Run the development server:**
   ```bash
   npm run dev
   ```

5. **Build for production:**
   ```bash
   npm run build
   npm start
   ```

## Code Style

### Backend

- **Black** for Python formatting
- **Flake8** for linting
- **MyPy** for type checking

Run formatters:
```bash
black app/
flake8 app/
mypy app/
```

### Frontend

- **ESLint** for linting
- **Prettier** for formatting (configured via Next.js)

Run linter:
```bash
npm run lint
```

## Database Migrations

When database models are added, use Alembic for migrations:

```bash
cd backend
# Generate migration
alembic revision --autogenerate -m "description"
# Apply migration
alembic upgrade head
```

## Testing

### Backend Tests

```bash
cd backend
pytest
pytest --cov=app  # With coverage
```

### Frontend Tests

Test framework to be added in future iterations.

## Debugging

### Backend

- FastAPI provides automatic docs at `/docs`
- Use Python debugger: `import pdb; pdb.set_trace()`
- Check logs in terminal output

### Frontend

- Use browser DevTools for debugging
- React DevTools extension recommended
- Next.js provides error overlays

## Common Issues

### Port Already in Use

If ports are already in use:
```bash
# Find process using port 8000
lsof -i :8000  # On Linux/Mac
netstat -ano | findstr :8000  # On Windows
# Kill the process or change the port in .env
```

### Database Connection Issues

- Ensure PostgreSQL is running
- Check DATABASE_URL in .env
- Verify database credentials

### Dependency Issues

- Clear virtual environment and reinstall
- Clear node_modules and reinstall
- Check Python/Node version compatibility

## Contributing

1. Create a feature branch
2. Make changes following code style guidelines
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit pull request
