"""Integration tests for FastAPI endpoints."""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestHealthEndpoint:
    """Test cases for health check endpoint."""

    def test_health_check_returns_200(self):
        """Test that health check returns 200 OK."""
        response = client.get("/health")
        assert response.status_code == 200

    def test_health_check_response_structure(self):
        """Test health check response structure."""
        response = client.get("/health")
        data = response.json()
        assert "status" in data
        assert "service" in data
        assert data["status"] == "healthy"
        assert data["service"] == "calculator"


class TestAddEndpoint:
    """Test cases for add endpoint."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        response = client.get("/add?x=5&y=3")
        assert response.status_code == 200
        data = response.json()
        assert data["operation"] == "add"
        assert data["x"] == 5
        assert data["y"] == 3
        assert data["result"] == 8

    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        response = client.get("/add?x=-5&y=-3")
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == -8

    def test_add_floats(self):
        """Test adding float numbers."""
        response = client.get("/add?x=5.5&y=3.2")
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == pytest.approx(8.7)

    def test_add_missing_parameter(self):
        """Test add with missing parameter returns 422."""
        response = client.get("/add?x=5")
        assert response.status_code == 422


class TestSubtractEndpoint:
    """Test cases for subtract endpoint."""

    def test_subtract_positive_numbers(self):
        """Test subtracting two positive numbers."""
        response = client.get("/subtract?x=10&y=4")
        assert response.status_code == 200
        data = response.json()
        assert data["operation"] == "subtract"
        assert data["result"] == 6

    def test_subtract_negative_result(self):
        """Test subtraction with negative result."""
        response = client.get("/subtract?x=3&y=10")
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == -7


class TestMultiplyEndpoint:
    """Test cases for multiply endpoint."""

    def test_multiply_positive_numbers(self):
        """Test multiplying two positive numbers."""
        response = client.get("/multiply?x=6&y=7")
        assert response.status_code == 200
        data = response.json()
        assert data["operation"] == "multiply"
        assert data["result"] == 42

    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        response = client.get("/multiply?x=5&y=0")
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 0


class TestDivideEndpoint:
    """Test cases for divide endpoint."""

    def test_divide_positive_numbers(self):
        """Test dividing two positive numbers."""
        response = client.get("/divide?x=20&y=4")
        assert response.status_code == 200
        data = response.json()
        assert data["operation"] == "divide"
        assert data["result"] == 5.0

    def test_divide_by_zero_returns_400(self):
        """Test that division by zero returns 400 error."""
        response = client.get("/divide?x=10&y=0")
        assert response.status_code == 400
        data = response.json()
        assert "detail" in data
        assert "Division by zero" in data["detail"]

    def test_divide_float_result(self):
        """Test division with float result."""
        response = client.get("/divide?x=10&y=3")
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == pytest.approx(3.333333333)


class TestCalcEndpoint:
    """Test cases for POST /calc endpoint."""

    def test_calc_add_operation(self):
        """Test /calc endpoint with add operation."""
        response = client.post(
            "/calc",
            json={"operation": "add", "x": 10, "y": 5},
        )
        assert response.status_code == 200
        data = response.json()
        assert data["operation"] == "add"
        assert data["result"] == 15

    def test_calc_subtract_operation(self):
        """Test /calc endpoint with subtract operation."""
        response = client.post(
            "/calc",
            json={"operation": "subtract", "x": 10, "y": 5},
        )
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 5

    def test_calc_multiply_operation(self):
        """Test /calc endpoint with multiply operation."""
        response = client.post(
            "/calc",
            json={"operation": "multiply", "x": 6, "y": 7},
        )
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 42

    def test_calc_divide_operation(self):
        """Test /calc endpoint with divide operation."""
        response = client.post(
            "/calc",
            json={"operation": "divide", "x": 20, "y": 4},
        )
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 5.0

    def test_calc_invalid_operation(self):
        """Test /calc endpoint with invalid operation."""
        response = client.post(
            "/calc",
            json={"operation": "power", "x": 2, "y": 3},
        )
        assert response.status_code == 400
        data = response.json()
        assert "detail" in data
        assert "Invalid operation" in data["detail"]

    def test_calc_divide_by_zero(self):
        """Test /calc endpoint with division by zero."""
        response = client.post(
            "/calc",
            json={"operation": "divide", "x": 10, "y": 0},
        )
        assert response.status_code == 400
        data = response.json()
        assert "Division by zero" in data["detail"]

    def test_calc_missing_fields(self):
        """Test /calc endpoint with missing fields."""
        response = client.post(
            "/calc",
            json={"operation": "add", "x": 10},
        )
        assert response.status_code == 422

    def test_calc_invalid_types(self):
        """Test /calc endpoint with invalid types."""
        response = client.post(
            "/calc",
            json={"operation": "add", "x": "not a number", "y": 5},
        )
        assert response.status_code == 422
