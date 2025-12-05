# 📝 EVOLUTION-OF-TODO

A sophisticated task management application evolving from console to full-stack web application with intelligent features.

[![Python](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![TypeScript](https://img.shields.io/badge/typescript-5.x-blue.svg)](https://www.typescriptlang.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/iamKhan79690/EVOLUTION-OF-TODO/actions)

## 🚀 Project Evolution

### Phase I: Console Application ✅
Advanced Python console application with intelligent task management
- **Features**: Priorities, tags, due dates, recurring tasks, search, reminders
- **Architecture**: Domain-driven design with clean separation of concerns
- **Testing**: 80%+ test coverage

### Phase II: Full-Stack Web Application ✅ (Development Setup Complete)
Modern web application with real-time collaboration and enhanced features
- **Frontend**: Next.js 16+ with TypeScript and Tailwind CSS
- **Backend**: FastAPI with SQLModel and Neon PostgreSQL
- **Authentication**: Better Auth with JWT integration
- **Status**: Development environment ready - both servers running

## 🌟 Phase II Features

**Modern Web Interface:**
- Responsive design with mobile support
- Real-time updates and notifications
- Advanced filtering and search capabilities

**Enhanced Task Management:**
- All Phase I features migrated to web
- User authentication and data persistence
- Collaborative task sharing (future)

**Developer Experience:**
- Hot reloading for rapid development
- Comprehensive testing suite
- Modern development tooling

## 🛠️ Phase II Setup

**Requirements:**
- Node.js 18.0+
- Python 3.11+
- Git

**Quick Setup (15 minutes):**
```bash
# Clone and setup
git clone <repository-url>
cd "The Evolution of Todo"
npm run setup

# Start development servers
npm run dev
```

**Current Development Environment:**
- **Frontend Server**: http://localhost:3000 ✅
- **Backend API**: http://localhost:8000 ✅
- **API Documentation**: http://localhost:8000/docs ✅
- **Health Check**: http://localhost:8000/api/v1/health ✅

**Individual Setup:**
```bash
# Clone and setup
git clone https://github.com/iamKhan79690/EVOLUTION-OF-TODO.git
cd EVOLUTION-OF-TODO

# Using UV (recommended)
uv sync && uv run src/main.py

# Or using pip
pip install -e . && python src/main.py
```

## 🌐 Phase II Development Environment

### Quick Start (15 minutes)
```bash
# 1. Clone repository
git clone https://github.com/iamKhan79690/EVOLUTION-OF-TODO.git
cd "The Evolution of Todo"

# 2. Run setup script (Unix/Linux/macOS)
./scripts/setup.sh

# OR (Windows)
scripts\setup.bat

# 3. Start development servers
npm run dev
```

### Manual Setup (if preferred)
```bash
# 1. Setup Frontend
cd frontend
npm install
npm run dev

# 2. Setup Backend (in new terminal)
cd backend
python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
python main.py
```

### Development Access Points
- **Frontend**: http://localhost:3000 (Next.js development server)
- **Backend API**: http://localhost:8000 (FastAPI development server)
- **API Documentation**: http://localhost:8000/docs (Interactive OpenAPI docs)
- **Health Check**: http://localhost:8000/api/v1/health (Service status monitoring)

### Environment Variables
Copy `.env.local.example` to `.env.local` and configure:
```bash
# Database
DATABASE_URL=postgresql://user:pass@ep-xyz.us-east-2.aws.neon.tech/dbname

# Authentication (generate secure secrets)
BETTER_AUTH_SECRET=your-32-character-secret-key
JWT_SECRET=your-jwt-secret-key
```

## 🚀 Phase I Usage

The app provides an intuitive menu-driven interface for managing tasks with advanced features:

**Main Operations:** Add, view, complete, delete, search, filter, and sort tasks.

**Task Creation Options:**
- Priority levels (High/Medium/Low)
- Custom tags for categorization
- Due dates with reminder notifications
- Recurring patterns (daily, weekly, monthly, yearly)

**Search & Organization:**
- Keyword search across all task fields
- Filter by priority, tags, or completion status
- Sort by priority, title, or due date

## 🏗️ Architecture

Clean, layered design with domain-driven principles:

**Domain Layer** (`src/domain/`)
- Task models with priority, tags, due dates, and recurrence
- Business rules and domain-specific exceptions

**Services Layer** (`src/services/`)
- Task orchestration and validation logic
- Recurrence and reminder management services

**UI Layer** (`src/ui/`)
- Console interface with menu navigation
- Formatted output with priority indicators

**Testing** (`tests/`)
- 80%+ coverage across domain, service, and integration layers

## 🧪 Testing

80%+ test coverage with comprehensive validation:

```bash
# Run tests
uv run pytest --cov=src --cov-report=term-missing

# Code quality
uv run ruff format src tests && uv run ruff check src tests
```

**Stack:** Python 3.13+, Pytest, Ruff, UV, Croniter

**Structure:** Domain → Services → UI → Tests (clean separation of concerns)

## 👥 Contributing

1. Fork and create a feature branch
2. Make changes with proper testing and documentation
3. Ensure tests pass (`uv run pytest`) and code quality standards
4. Submit a Pull Request

**Standards:** Type hints, docstrings, PEP 8, 80%+ test coverage, descriptive commits

## 🚀 Roadmap

**Current (Phase I):** ✅ Core task management with priorities, tags, due dates, recurring tasks, and search capabilities

**Planned (Phase II):** Persistent storage, enhanced TUI, authentication, export/import

## 📄 License

MIT License - see [LICENSE](LICENSE) for details

---

<p align="center">Built with ❤️ using Python | © 2025 EVOLUTION-OF-TODO</p>