# FastAPI Calculator - Quick Reference

## Setup Commands

```bash
# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Configure and install
poetry config virtualenvs.in-project true
poetry install

# Install Playwright
poetry run playwright install --with-deps

# Activate environment
poetry shell
```

## Run Commands

```bash
# Start server
poetry run uvicorn app.main:app --reload

# Or use the script
chmod +x start.sh
./start.sh
```

## Test Commands

```bash
# All tests
poetry run pytest -v

# Unit tests only
poetry run pytest tests/unit/ -v

# Integration tests only
poetry run pytest tests/integration/ -v

# E2E tests only
poetry run pytest tests/e2e/ -v

# With coverage
poetry run pytest --cov=. --cov-report=html
```

## Useful URLs

- Web UI: http://localhost:8000/
- API Docs: http://localhost:8000/docs
- Health: http://localhost:8000/health

## Git Workflow

```bash
# Create feature branch
git checkout -b feature/my-feature

# Commit with conventional format
git commit -m "feat: add new feature"
git commit -m "test: add tests for feature"
git commit -m "fix: resolve bug"

# Push and create PR
git push origin feature/my-feature
```

## Troubleshooting

```bash
# Kill server on port 8000
lsof -i :8000
kill -9 <PID>

# Reset environment
poetry env remove python
poetry install

# Reinstall Playwright
poetry run playwright install --with-deps
```
