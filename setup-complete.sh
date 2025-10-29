#!/bin/bash
# Complete Setup and Verification Script
# Run this to set up everything from scratch

set -e  # Exit on error

echo "========================================"
echo "FastAPI Calculator - Complete Setup"
echo "========================================"
echo ""

# Check if Poetry is installed
echo "1️⃣  Checking Poetry installation..."
if ! command -v poetry &> /dev/null; then
    echo "❌ Poetry not found. Installing..."
    curl -sSL https://install.python-poetry.org | python3 -
    export PATH="/root/.local/bin:$PATH"
    echo 'export PATH="/root/.local/bin:$PATH"' >> ~/.bashrc
    echo "✅ Poetry installed"
else
    echo "✅ Poetry already installed"
fi

# Verify Poetry
poetry --version

echo ""
echo "2️⃣  Configuring Poetry..."
poetry config virtualenvs.in-project true
echo "✅ Poetry configured for in-project virtualenv"

echo ""
echo "3️⃣  Installing dependencies (this may take a few minutes)..."
poetry install --no-interaction
echo "✅ Dependencies installed"

echo ""
echo "4️⃣  Installing Playwright browsers..."
poetry run playwright install --with-deps
echo "✅ Playwright browsers installed"

echo ""
echo "5️⃣  Running verification tests..."
echo ""
echo "   Running unit tests..."
poetry run pytest tests/unit/ -v --tb=short
echo "✅ Unit tests passed"

echo ""
echo "   Running integration tests..."
poetry run pytest tests/integration/ -v --tb=short
echo "✅ Integration tests passed"

echo ""
echo "6️⃣  Checking test coverage..."
poetry run pytest tests/unit/ --cov=domain --cov-report=term-missing --cov-fail-under=80 -q
echo "✅ Coverage check passed"

echo ""
echo "========================================"
echo "✅ SETUP COMPLETE!"
echo "========================================"
echo ""
echo "📋 Next Steps:"
echo ""
echo "1. Start the application:"
echo "   poetry run uvicorn app.main:app --reload"
echo ""
echo "2. Visit in your browser:"
echo "   http://localhost:8000/"
echo ""
echo "3. View API documentation:"
echo "   http://localhost:8000/docs"
echo ""
echo "4. Run E2E tests (requires app to be running):"
echo "   # In another terminal:"
echo "   poetry run pytest tests/e2e/ -v"
echo ""
echo "5. Activate virtual environment for development:"
echo "   poetry shell"
echo ""
echo "📚 Read these files for more information:"
echo "   - NEXT_STEPS.md - Detailed next steps guide"
echo "   - README.md - Complete documentation"
echo "   - QUICKSTART.md - Quick command reference"
echo ""
echo "🎉 Happy coding!"
