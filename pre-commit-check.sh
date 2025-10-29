#!/bin/bash
# Pre-commit checklist script

echo "🔍 Pre-Commit Checklist"
echo "======================="

# Check if venv is active
if [[ "$VIRTUAL_ENV" == *".venv"* ]]; then
    echo "✅ Virtual environment active"
else
    echo "❌ Virtual environment NOT active - run 'poetry shell'"
    exit 1
fi

# Check Python path
PYTHON_PATH=$(which python)
if [[ "$PYTHON_PATH" == *".venv"* ]]; then
    echo "✅ Using correct Python: $PYTHON_PATH"
else
    echo "❌ Wrong Python path: $PYTHON_PATH"
    exit 1
fi

# Run tests
echo ""
echo "🧪 Running tests..."
poetry run pytest tests/unit/ tests/integration/ -v --tb=short

if [ $? -eq 0 ]; then
    echo "✅ All tests passed"
else
    echo "❌ Tests failed"
    exit 1
fi

# Check coverage
echo ""
echo "📊 Checking coverage..."
poetry run pytest tests/unit/ --cov=domain --cov-report=term-missing --cov-fail-under=90 -q

if [ $? -eq 0 ]; then
    echo "✅ Coverage threshold met (>90%)"
else
    echo "⚠️  Coverage below threshold"
fi

echo ""
echo "✅ Pre-commit checks complete!"
echo ""
echo "Ready to commit? Run:"
echo "  git add ."
echo "  git commit -m 'type: your message'"
