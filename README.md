# Sutradhar

> **Every transaction tells a story. Tracing the hidden flow of money.**

Sutradhar is an AI-powered financial intelligence platform that extracts, standardizes, analyzes, and investigates bank statements. The platform will eventually support OCR, fraud detection, fund flow tracing, graph intelligence, risk scoring, and evidence-ready reporting.

---

## 🛠️ Tech Stack

| Component | Technology |
| --- | --- |
| **Frontend** | Next.js 15, React, TypeScript, Tailwind CSS |
| **Backend** | FastAPI, Python 3.12 |
| **Database** | PostgreSQL |
| **Authentication** | JWT (python-jose), bcrypt (passlib) |
| **Infrastructure** | Docker, Docker Compose |

---

## � Project Structure

```text
sutradhar/
├── backend/
│   ├── app/
│   │   ├── api/          # API endpoints and routing
│   │   ├── core/         # Configuration and settings
│   │   ├── models/       # SQLAlchemy database models
│   │   ├── schemas/      # Pydantic schemas for validation
│   │   ├── services/     # Business logic layer
│   │   ├── repositories/ # Data access layer
│   │   ├── database/     # Database session management
│   │   ├── middleware/   # Custom middleware
│   │   └── main.py       # Application entry point
│   ├── tests/            # Test suite
│   ├── requirements.txt  # Python dependencies
│   ├── Dockerfile        # Backend container configuration
│   └── .env.example      # Environment variables template
├── frontend/
│   ├── src/
│   │   ├── app/          # Next.js app router pages
│   │   ├── components/   # Reusable React components
│   │   ├── services/     # API client services
│   │   ├── hooks/        # Custom React hooks
│   │   ├── lib/          # Utility functions
│   │   ├── types/        # TypeScript type definitions
│   │   └── styles/       # Global styles
│   ├── public/           # Static assets
│   ├── package.json      # Node dependencies
│   ├── Dockerfile        # Frontend container configuration
│   └── .env.example      # Environment variables template
├── infrastructure/
│   ├── docker/
│   │   ├── postgres/     # PostgreSQL configuration
│   │   └── nginx/        # Reverse proxy configuration
│   └── README.md         # Infrastructure documentation
├── docs/                 # Project documentation
│   ├── ARCHITECTURE.md   # Architecture documentation
│   ├── API.md            # API documentation
│   └── DEVELOPMENT.md   # Development guide
├── scripts/              # Utility scripts
│   ├── setup.sh          # Linux/Mac setup script
│   ├── setup.ps1         # Windows setup script
│   ├── dev.sh            # Linux/Mac development script
│   ├── dev.ps1           # Windows development script
│   ├── test.sh           # Linux/Mac test script
│   ├── test.ps1          # Windows test script
│   └── README.md         # Scripts documentation
├── .github/              # GitHub workflows
├── docker-compose.yml    # Docker orchestration
├── .gitignore           # Git ignore rules
├── .env.example          # Root environment variables
└── README.md             # This file
```

---

## � Authentication

Sutradhar implements a production-ready JWT-based authentication system with role-based access control (RBAC).

### Features

- **JWT Authentication**: Secure token-based authentication using python-jose
- **Password Hashing**: bcrypt for secure password storage
- **Role-Based Access Control**: ADMIN, INVESTIGATOR, ANALYST, VIEWER roles
- **Audit Logging**: Track all user actions for compliance
- **Protected Routes**: Frontend and backend route protection

### API Endpoints

- `POST /api/v1/auth/register` - Register new user
- `POST /api/v1/auth/login` - Login and receive JWT token
- `GET /api/v1/auth/me` - Get current authenticated user

### User Roles

- **ADMIN**: Full system access, user management
- **INVESTIGATOR**: Case investigation access
- **ANALYST**: Data analysis access
- **VIEWER**: Read-only access

### Frontend Authentication

The frontend includes:
- Login page at `/login`
- Registration page at `/register`
- Protected dashboard at `/dashboard`
- AuthContext for global authentication state
- Automatic token management and refresh

### Database Setup

Run database migrations to create authentication tables:

```bash
cd backend
alembic upgrade head
```

Or initialize the database with seed data:

```bash
python -m app.database.init_db
```

This creates a default admin user:
- Email: `admin@sutradhar.com`
- Password: `admin123`

**Important**: Change the default admin password in production.

---

## � Quick Start with Docker

### Prerequisites

- Docker Desktop installed
- Docker Compose installed

### Setup

1. **Clone the repository:**
```bash
git clone https://github.com/vallabhatech/sutradhar.git
cd sutradhar
```

2. **Create your local environment file:**
```bash
cp .env.example .env
```

> On Windows PowerShell, use `Copy-Item .env.example .env`. Set a strong `POSTGRES_PASSWORD` and `SECRET_KEY` before using the stack beyond local development.

3. **Run the setup script:**

**Linux/Mac:**
```bash
chmod +x scripts/setup.sh
./scripts/setup.sh
```

**Windows:**
```powershell
.\scripts\setup.ps1
```

4. **Access the application:**
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

### Docker Commands

```bash
# Start all services
docker-compose up -d

# Stop all services
docker-compose down

# View logs
docker-compose logs -f

# Restart a specific service
docker-compose restart backend

# Rebuild and start
docker-compose up -d --build
```

---

## 💻 Local Development Setup

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

---

## 🔧 Configuration

### Environment Variables

**Root .env.example:**
```env
DATABASE_URL=postgresql+asyncpg://sutradhar:sutradhar_password@localhost:5432/sutradhar
SECRET_KEY=your-secret-key-change-in-production
APP_ENV=development
API_PORT=8000
NEXT_PUBLIC_API_URL=http://localhost:8000
```

**Backend .env.example:**
```env
DATABASE_URL=postgresql+asyncpg://sutradhar:sutradhar_password@localhost:5432/sutradhar
SECRET_KEY=your-secret-key-change-in-production
APP_ENV=development
API_PORT=8000
```

**Frontend .env.example:**
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

---

## 📚 Documentation

- [Architecture Documentation](docs/ARCHITECTURE.md) - System architecture and design patterns
- [API Documentation](docs/API.md) - API endpoints and usage
- [Development Guide](docs/DEVELOPMENT.md) - Development setup and best practices
- [Infrastructure Documentation](infrastructure/README.md) - Docker and infrastructure setup
- [Scripts Documentation](scripts/README.md) - Utility scripts usage

---

## 🧪 Testing

### Backend Tests

```bash
cd backend
pytest
pytest --cov=app  # With coverage
```

### Frontend Tests

Test framework to be added in future iterations.

---

## 🗺️ Roadmap

### Phase 1 — Foundation
- [x] Project structure and development environment
- [x] FastAPI backend
- [x] Next.js frontend
- [x] PostgreSQL database setup
- [x] Docker containerization
- [x] JWT authentication and RBAC
- [x] Audit logging
- [x] Alembic migration support

### Phase 2 — Core Intelligence
- [ ] Bank statement upload and parsing
- [ ] OCR integration
- [ ] Transaction normalization
- [ ] Rule-based fraud detection
- [ ] Case management and investigation workflows

### Phase 3 — Advanced Intelligence
- [ ] Graph-based fund-flow analysis
- [ ] AI-assisted transaction investigation
- [ ] Risk scoring
- [ ] Evidence-ready reporting
- [ ] Scalable asynchronous processing

---

## 🛡️ Security Notes

- Never commit secrets or credentials to version control
- Use strong, unique secrets in production
- Change default admin password before deployment
- Enable HTTPS in production environments
- Regularly update dependencies for security patches
- Never use real banking data during development or testing
- Implement rate limiting on authentication endpoints
- Use environment-specific SECRET_KEY values

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. Create a feature branch from main
2. Make changes following the existing code style
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request with a clear description

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for the full text.

---

## 📞 Support

For questions or issues, please open an issue on GitHub or contact the development team.
