"""E2E tests using Playwright for browser automation."""
import pytest
from playwright.sync_api import Page, expect
import subprocess
import time
import requests


@pytest.fixture(scope="module")
def server():
    """Start FastAPI server for E2E tests."""
    # Start server in background
    process = subprocess.Popen(
        ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    # Wait for server to be ready
    max_retries = 30
    for _ in range(max_retries):
        try:
            response = requests.get("http://localhost:8000/health")
            if response.status_code == 200:
                break
        except requests.exceptions.ConnectionError:
            time.sleep(1)
    else:
        process.terminate()
        raise RuntimeError("Server failed to start")

    yield process

    # Cleanup
    process.terminate()
    process.wait()


def test_calculator_ui_addition(page: Page, server):
    """Test calculator UI for addition operation."""
    # Navigate to the calculator page
    page.goto("http://localhost:8000/")

    # Wait for page to load
    expect(page.locator("h1")).to_contain_text("FastAPI Calculator")

    # Fill in the form
    page.locator("#input-x").fill("15")
    page.locator("#input-y").fill("7")
    page.locator("#operation-select").select_option("add")

    # Click calculate button
    page.locator("#calculate-button").click()

    # Wait for result to appear
    result_display = page.locator("#result-display")
    expect(result_display).to_be_visible(timeout=5000)

    # Assert the result contains the expected value
    expect(result_display).to_contain_text("22")


def test_calculator_ui_subtraction(page: Page, server):
    """Test calculator UI for subtraction operation."""
    page.goto("http://localhost:8000/")

    page.locator("#input-x").fill("20")
    page.locator("#input-y").fill("8")
    page.locator("#operation-select").select_option("subtract")

    page.locator("#calculate-button").click()

    result_display = page.locator("#result-display")
    expect(result_display).to_be_visible(timeout=5000)
    expect(result_display).to_contain_text("12")


def test_calculator_ui_multiplication(page: Page, server):
    """Test calculator UI for multiplication operation."""
    page.goto("http://localhost:8000/")

    page.locator("#input-x").fill("6")
    page.locator("#input-y").fill("7")
    page.locator("#operation-select").select_option("multiply")

    page.locator("#calculate-button").click()

    result_display = page.locator("#result-display")
    expect(result_display).to_be_visible(timeout=5000)
    expect(result_display).to_contain_text("42")


def test_calculator_ui_division(page: Page, server):
    """Test calculator UI for division operation."""
    page.goto("http://localhost:8000/")

    page.locator("#input-x").fill("20")
    page.locator("#input-y").fill("4")
    page.locator("#operation-select").select_option("divide")

    page.locator("#calculate-button").click()

    result_display = page.locator("#result-display")
    expect(result_display).to_be_visible(timeout=5000)
    expect(result_display).to_contain_text("5")


def test_calculator_ui_division_by_zero_error(page: Page, server):
    """Test calculator UI shows error for division by zero."""
    page.goto("http://localhost:8000/")

    page.locator("#input-x").fill("10")
    page.locator("#input-y").fill("0")
    page.locator("#operation-select").select_option("divide")

    page.locator("#calculate-button").click()

    # Wait for error to appear
    error_display = page.locator("#error-display")
    expect(error_display).to_be_visible(timeout=5000)
    expect(error_display).to_contain_text("Division by zero")


def test_calculator_ui_page_elements(page: Page, server):
    """Test that all required UI elements are present."""
    page.goto("http://localhost:8000/")

    # Check title
    expect(page.locator("h1")).to_be_visible()

    # Check input fields
    expect(page.locator("#input-x")).to_be_visible()
    expect(page.locator("#input-y")).to_be_visible()

    # Check operation selector
    expect(page.locator("#operation-select")).to_be_visible()

    # Check calculate button
    expect(page.locator("#calculate-button")).to_be_visible()

    # Check link to API docs
    expect(page.locator("a[href='/docs']")).to_be_visible()
