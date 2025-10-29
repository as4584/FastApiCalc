# FastAPI Calculator - IS218 Midterm Project

[![CI Pipeline](https://github.com/as4584/midterm/actions/workflows/ci.yml/badge.svg)](https://github.com/as4584/midterm/actions/workflows/ci.yml)

A production-ready calculator API built with FastAPI, demonstrating SOLID design principles, comprehensive testing (TDD), and modern CI/CD practices.

## 🎯 Overview

This project implements a RESTful calculator API with:
- **SOLID Design Principles**: Strategy pattern for operations, Dependency Inversion, Single Responsibility
- **Comprehensive Testing**: Unit tests (>90% coverage), Integration tests, E2E browser automation
- **Structured Logging**: JSON-formatted logs with request correlation
- **CI/CD Pipeline**: Automated testing and deployment via GitHub Actions
- **Modern Stack**: FastAPI, Pydantic v2, Poetry, pytest, Playwright

## 📋 Prerequisites

- Python 3.10 or higher
- Poetry package manager
- Git for version control
- Chrome/Chromium browser (for E2E tests)

## 🚀 Installation & Setup

### 1. Install Poetry

```bash
# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH (add to ~/.bashrc for persistence)
export PATH="/root/.local/bin:$PATH"

# Verify installation
poetry --version
```

### 2. Clone Repository

```bash
git clone https://github.com/as4584/midterm.git
cd midterm
```

### 3. Configure Virtual Environment

```bash
# Configure Poetry to create venv in project directory
poetry config virtualenvs.in-project true

# Install dependencies
poetry install

# Verify installation
poetry show
```

### 4. Activate Environment

```bash
# Activate virtual environment
poetry shell

# Verify activation (should show .venv/bin/python)
which python
```

### 5. Install Playwright Browsers (for E2E tests)

```bash
# Install browsers and system dependencies
poetry run playwright install --with-deps
```

## 🎮 Running the Application

### Start Development Server

```bash
# Using Poetry
poetry run uvicorn app.main:app --reload --port 8000

# Or if already in poetry shell
uvicorn app.main:app --reload --port 8000
```

### Access the Application

- **Web UI**: http://localhost:8000/
- **API Documentation**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

### Example API Calls

```bash
# Using query parameters
curl "http://localhost:8000/add?x=5&y=3"
curl "http://localhost:8000/subtract?x=10&y=4"
curl "http://localhost:8000/multiply?x=6&y=7"
curl "http://localhost:8000/divide?x=20&y=4"

# Using POST /calc endpoint
curl -X POST http://localhost:8000/calc \
  -H "Content-Type: application/json" \
  -d '{"operation":"add","x":10,"y":5}'
```

## 🧪 Testing Strategy

### Run All Tests

```bash
# Run complete test suite
poetry run pytest -v

# Run with coverage report
poetry run pytest --cov=. --cov-report=html
```

### Unit Tests (Domain Logic)

```bash
# Run unit tests only
poetry run pytest tests/unit/ -v

# Run with coverage
poetry run pytest tests/unit/ -v --cov=domain --cov-report=term
```

**Coverage**: 
- ✅ All arithmetic operations (add, subtract, multiply, divide)
- ✅ Edge cases: negatives, floats, large numbers, division by zero
- ✅ Operation factory pattern
- ✅ Calculator service orchestration

### Integration Tests (API Endpoints)

```bash
# Run integration tests
poetry run pytest tests/integration/ -v

# Run with coverage
poetry run pytest tests/integration/ -v --cov=app --cov-report=term
```

**Coverage**:
- ✅ All FastAPI endpoints with TestClient
- ✅ HTTP status codes validation (200, 400, 422)
- ✅ Response structure validation
- ✅ Error handling scenarios

### E2E Tests (Playwright Browser Automation)

```bash
# Ensure Playwright browsers are installed first
poetry run playwright install --with-deps

# Run E2E tests
poetry run pytest tests/e2e/ -v

# Run with headed browser (visible)
poetry run pytest tests/e2e/ -v --headed
```

**Coverage**:
- ✅ Browser UI interaction testing
- ✅ Form submission workflows
- ✅ Result display validation
- ✅ Error message scenarios

### Generate HTML Coverage Report

```bash
poetry run pytest --cov=. --cov-report=html
open htmlcov/index.html  # or xdg-open on Linux
```

## 📊 Logging Implementation

### Structured Logging Policy

- **Format**: JSON-structured logs to stdout (container-friendly)
- **Fields**: `timestamp`, `level`, `logger`, `message`, `request_id`, operation details
- **Levels Used**:
  - `INFO`: Request lifecycle, successful operations
  - `WARNING`: Validation errors, deprecations
  - `ERROR`: Failed operations, exceptions
  - `DEBUG`: Internal state (development only)

### View Logs

```bash
# Start server with logging
poetry run uvicorn app.main:app --log-level info

# Example log output:
# {"timestamp": "2025-10-28T14:32:01.123Z", "level": "INFO", "logger": "fastapi_calculator", "message": "Calculation completed", "operation": "add", "x": 5.0, "y": 3.0, "result": 8.0}
```

## 🔄 Git Workflow

### Branching Strategy

- `main`: Production-ready code
- `feature/*`: New features and implementations
- `test/*`: Test additions
- `docs/*`: Documentation updates

### Conventional Commits

We follow conventional commit format:

```bash
# Format: <type>: <subject>

feat: add exponentiation operation
test: add unit tests for new operation
fix: resolve division precision issue
chore: update logging configuration
ci: add coverage threshold check
docs: update README with examples
```

### Example Workflow

```bash
# Create feature branch
git checkout -b feature/new-operation

# Make changes and commit
git add .
git commit -m "feat: add modulo operation"

# Push and create PR
git push origin feature/new-operation
```

## 🔧 CI/CD Pipeline

### GitHub Actions Workflow

**Triggers**: Every push and pull request to `main` branch

**Pipeline Steps**:
1. Checkout code
2. Setup Python 3.11
3. Install Poetry and configure
4. Cache dependencies for faster builds
5. Install project dependencies
6. Install Playwright browsers
7. Run unit tests with coverage
8. Run integration tests
9. Start server in background
10. Run E2E tests with browser automation
11. Upload test reports and coverage
12. Cleanup and generate artifacts

### View CI Status

- Navigate to: https://github.com/as4584/midterm/actions
- Check workflow runs for status
- Green checkmark = all tests passing ✅

### CI Configuration

See `.github/workflows/ci.yml` for complete pipeline configuration.

## 📁 Project Structure

```
FastApiCalc_is218/
├── app/                          # FastAPI application layer
│   ├── __init__.py
│   ├── main.py                   # FastAPI app entry point
│   ├── api/
│   │   └── endpoints/
│   │       └── calculator.py     # API route handlers
│   ├── core/
│   │   ├── config.py             # App configuration
│   │   └── dependencies.py       # Dependency injection
│   └── static/
│       ├── index.html            # Calculator UI
│       ├── style.css             # Styling
│       └── script.js             # Frontend logic
├── domain/                       # Business logic (framework-agnostic)
│   ├── __init__.py
│   ├── interfaces/
│   │   ├── operations.py         # IOperation interface
│   │   └── logger.py             # ILogger interface
│   ├── models/
│   │   ├── request.py            # Pydantic request models
│   │   └── response.py           # Pydantic response models
│   ├── operations/
│   │   ├── basic.py              # Concrete operations (Add, Sub, Mul, Div)
│   │   └── factory.py            # Operation factory
│   └── services/
│       ├── calculator.py         # Calculator service
│       └── logger.py             # Structured logger implementation
├── tests/                        # Test suites
│   ├── unit/                     # Domain logic tests
│   │   ├── test_operations.py
│   │   └── test_calculator.py
│   ├── integration/              # API endpoint tests
│   │   └── test_api.py
│   └── e2e/                      # Playwright browser tests
│       └── test_ui.py
├── docs/
│   └── screenshots/              # Grading screenshots
│       ├── ci-green.png          # CI workflow passing
│       └── app-running.png       # App in browser
├── .github/
│   └── workflows/
│       └── ci.yml                # GitHub Actions pipeline
├── pyproject.toml                # Poetry dependencies & config
├── .gitignore
└── README.md                     # This file
```

## 🏗️ Architecture & Design Patterns

### SOLID Principles Applied

**Single Responsibility**:
- Each operation class handles one arithmetic function
- Services separated from HTTP handlers
- Logging isolated in dedicated service

**Open/Closed**:
- Strategy pattern allows adding operations without modifying existing code
- Factory pattern enables extension

**Liskov Substitution**:
- All operations implement `IOperation` interface
- Interchangeable operation strategies

**Interface Segregation**:
- Focused interfaces: `IOperation`, `ILogger`
- Minimal method contracts

**Dependency Inversion**:
- High-level modules depend on abstractions
- Logger and factory injected as dependencies

### Design Patterns

**Strategy Pattern**: Arithmetic operations as interchangeable strategies

```python
# Each operation implements IOperation interface
class AddOperation(IOperation):
    def execute(self, x: float, y: float) -> float:
        return x + y
```

**Factory Pattern**: OperationFactory resolves operations by name

```python
factory = OperationFactory()
operation = factory.get_operation("add")
result = operation.execute(5, 3)
```

**Dependency Injection**: FastAPI `Depends()` for service injection

```python
@router.post("/calc")
async def calculate(
    request: CalculationRequest,
    calculator: CalculatorService = Depends(get_calculator_service),
):
    return calculator.calculate(...)
```

## ✅ Submission Checklist

### Code Quality
- [x] All tests passing locally and in CI
- [x] Code follows SOLID principles
- [x] Strategy pattern implemented for operations
- [x] Structured JSON logging enabled
- [x] >90% test coverage

### Testing
- [x] Unit tests for domain logic
- [x] Integration tests for all API endpoints
- [x] E2E tests with Playwright browser automation
- [x] CI pipeline green on GitHub Actions

### Documentation
- [x] Comprehensive README
- [x] Code comments for complex logic
- [x] API documentation via FastAPI /docs

### Deliverables
- [x] Repository URL: https://github.com/as4584/midterm
- [x] Screenshot: CI workflow passing (green)
- [x] Screenshot: Application running in browser

## 📸 Screenshots

### GitHub Actions - CI Pipeline (Green)

**Location**: `docs/screenshots/ci-green.png`

Shows all test jobs passing with green checkmarks:
- Unit tests with >90% coverage
- Integration tests for all endpoints
- E2E browser automation tests
- Successful artifact uploads

![CI Workflow Green](./docs/screenshots/ci-green.png)

### Application Running - Calculator in Action

**Location**: `docs/screenshots/app-running.png`

Shows calculator UI performing a calculation:
- Form filled with operands (x=15, y=7)
- Operation selected (addition)
- Result displayed (22)
- Clean, professional interface

![App Running](./docs/screenshots/app-running.png)

## 🐛 Troubleshooting

### Common Issues

**Port Already in Use**:
```bash
# Find process using port 8000
lsof -i :8000

# Kill the process
kill -9 <PID>

# Or use different port
poetry run uvicorn app.main:app --port 8001
```

**Virtual Environment Not Active**:
```bash
# Check which Python
which python
# Should show: /root/FastApiCalc_is218/.venv/bin/python

# If not, activate
poetry shell

# Verify prompt shows (.venv)
```

**Playwright Browsers Missing**:
```bash
# Install browsers and dependencies
poetry run playwright install --with-deps

# Verify
poetry run playwright --version
```

**Tests Failing Locally**:
```bash
# Ensure no server is running
pkill -f uvicorn

# Clear cache and reinstall
poetry env remove python
poetry install
poetry run playwright install --with-deps

# Run tests again
poetry run pytest -v
```

## 🔐 Anti-Leak Checklist

Before any `pip install` or package command, verify:

- [ ] `which python` → Shows `.venv/bin/python`
- [ ] `poetry shell` active (prompt shows `.venv`)
- [ ] Always use `poetry add <package>` instead of `pip install`
- [ ] `pip list` shows only project dependencies
- [ ] `echo $VIRTUAL_ENV` → Shows project venv path

## 📚 Technology Stack

- **Framework**: FastAPI 0.104.1
- **ASGI Server**: Uvicorn 0.24.0
- **Validation**: Pydantic 2.5.0
- **Testing**: pytest 7.4.3, httpx 0.25.2
- **E2E Testing**: Playwright (pytest-playwright 0.4.3)
- **Coverage**: pytest-cov 4.1.0
- **Package Manager**: Poetry
- **CI/CD**: GitHub Actions
- **Python**: 3.10+

## 👤 Author

**Your Name**  
IS218 - Fall 2025  
Midterm Project

## 📄 License

This project is created for educational purposes as part of IS218 coursework.

## 🙏 Acknowledgments

- IS218 Course Materials
- FastAPI Documentation
- Playwright Testing Framework
- Poetry Dependency Management
