#!/bin/bash
# Quick start script for the application

echo "🚀 Starting FastAPI Calculator"
echo "=============================="

# Check if Poetry is installed
if ! command -v poetry &> /dev/null; then
    echo "❌ Poetry is not installed"
    echo "Install with: curl -sSL https://install.python-poetry.org | python3 -"
    exit 1
fi

# Check if venv exists
if [ ! -d ".venv" ]; then
    echo "📦 Installing dependencies..."
    poetry config virtualenvs.in-project true
    poetry install
fi

# Start the server
echo ""
echo "✅ Starting server..."
echo "   Web UI: http://localhost:8000/"
echo "   API Docs: http://localhost:8000/docs"
echo ""
poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
