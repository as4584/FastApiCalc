// Calculator UI JavaScript
const form = document.getElementById('calculatorForm');
const resultContainer = document.getElementById('result-container');
const errorContainer = document.getElementById('error-container');
const resultDisplay = document.getElementById('result-display');
const errorDisplay = document.getElementById('error-display');
const loading = document.getElementById('loading');
const calculateButton = document.getElementById('calculate-button');

// Handle form submission
form.addEventListener('submit', async (e) => {
    e.preventDefault();

    // Get form values
    const x = parseFloat(document.getElementById('input-x').value);
    const y = parseFloat(document.getElementById('input-y').value);
    const operation = document.getElementById('operation-select').value;

    // Validate inputs
    if (!operation) {
        showError('Please select an operation');
        return;
    }

    // Hide previous results
    hideResults();

    // Show loading
    loading.classList.remove('hidden');
    calculateButton.disabled = true;

    try {
        // Call API
        const response = await fetch('/calc', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                operation: operation,
                x: x,
                y: y
            })
        });

        const data = await response.json();

        if (response.ok) {
            // Show result
            showResult(data.result, operation, x, y);
        } else {
            // Show error
            showError(data.detail || 'An error occurred');
        }
    } catch (error) {
        showError('Network error: Could not connect to server');
        console.error('Error:', error);
    } finally {
        // Hide loading
        loading.classList.add('hidden');
        calculateButton.disabled = false;
    }
});

function showResult(result, operation, x, y) {
    const operationSymbols = {
        'add': '+',
        'subtract': '−',
        'multiply': '×',
        'divide': '÷'
    };

    const symbol = operationSymbols[operation] || operation;
    resultDisplay.innerHTML = `
        <div style="margin-bottom: 10px; font-size: 1.2rem; color: #666;">
            ${x} ${symbol} ${y} =
        </div>
        <div>${result}</div>
    `;
    resultContainer.classList.remove('hidden');
    errorContainer.classList.add('hidden');
}

function showError(message) {
    errorDisplay.textContent = message;
    errorContainer.classList.remove('hidden');
    resultContainer.classList.add('hidden');
}

function hideResults() {
    resultContainer.classList.add('hidden');
    errorContainer.classList.add('hidden');
}

// Add keyboard shortcut for calculation (Enter)
document.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !calculateButton.disabled) {
        form.dispatchEvent(new Event('submit'));
    }
});
