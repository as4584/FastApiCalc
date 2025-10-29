"""Unit tests for arithmetic operations."""
import pytest
from domain.operations.basic import (
    AddOperation,
    SubtractOperation,
    MultiplyOperation,
    DivideOperation,
)


class TestAddOperation:
    """Test cases for AddOperation."""

    @pytest.mark.parametrize(
        "x,y,expected",
        [
            (5, 3, 8),  # Positive integers
            (-5, -3, -8),  # Negative integers
            (-5, 3, -2),  # Mixed signs
            (5.5, 3.2, 8.7),  # Floats
            (1e10, 1e10, 2e10),  # Large values
            (0, 5, 5),  # Zero cases
            (5, 0, 5),  # Zero cases
            (0, 0, 0),  # Both zero
        ],
    )
    def test_add_operation(self, x, y, expected):
        """Test addition with various inputs."""
        operation = AddOperation()
        result = operation.execute(x, y)
        assert result == pytest.approx(expected, rel=1e-9)

    def test_add_operation_name(self):
        """Test operation name."""
        operation = AddOperation()
        assert operation.name == "add"


class TestSubtractOperation:
    """Test cases for SubtractOperation."""

    @pytest.mark.parametrize(
        "x,y,expected",
        [
            (10, 3, 7),  # Positive integers
            (3, 10, -7),  # Negative result
            (-5, -3, -2),  # Both negative
            (-5, 3, -8),  # Mixed signs
            (10.5, 3.2, 7.3),  # Floats
            (1e10, 5e9, 5e9),  # Large values
            (5, 0, 5),  # Subtract zero
            (0, 5, -5),  # Subtract from zero
        ],
    )
    def test_subtract_operation(self, x, y, expected):
        """Test subtraction with various inputs."""
        operation = SubtractOperation()
        result = operation.execute(x, y)
        assert result == pytest.approx(expected, rel=1e-9)

    def test_subtract_operation_name(self):
        """Test operation name."""
        operation = SubtractOperation()
        assert operation.name == "subtract"


class TestMultiplyOperation:
    """Test cases for MultiplyOperation."""

    @pytest.mark.parametrize(
        "x,y,expected",
        [
            (5, 3, 15),  # Positive integers
            (-5, -3, 15),  # Negative × negative
            (-5, 3, -15),  # Negative × positive
            (2.5, 4.0, 10.0),  # Floats
            (1e6, 1e6, 1e12),  # Large values
            (5, 0, 0),  # Multiply by zero
            (0, 5, 0),  # Zero × number
            (0, 0, 0),  # Both zero
        ],
    )
    def test_multiply_operation(self, x, y, expected):
        """Test multiplication with various inputs."""
        operation = MultiplyOperation()
        result = operation.execute(x, y)
        assert result == pytest.approx(expected, rel=1e-9)

    def test_multiply_operation_name(self):
        """Test operation name."""
        operation = MultiplyOperation()
        assert operation.name == "multiply"


class TestDivideOperation:
    """Test cases for DivideOperation."""

    @pytest.mark.parametrize(
        "x,y,expected",
        [
            (10, 2, 5.0),  # Positive integers
            (10, 3, 3.333333333),  # Float result
            (-10, 2, -5.0),  # Negative dividend
            (-10, -2, 5.0),  # Both negative
            (7.5, 2.5, 3.0),  # Floats
            (1e12, 1e6, 1e6),  # Large values
            (1, 3, 0.333333333),  # Repeating decimal
        ],
    )
    def test_divide_operation(self, x, y, expected):
        """Test division with various inputs."""
        operation = DivideOperation()
        result = operation.execute(x, y)
        assert result == pytest.approx(expected, rel=1e-9)

    @pytest.mark.parametrize(
        "x,y",
        [
            (10, 0),  # Divide by zero
            (-10, 0),  # Negative divide by zero
            (0, 0),  # Zero divide by zero
        ],
    )
    def test_divide_by_zero_raises_exception(self, x, y):
        """Test that division by zero raises ValueError."""
        operation = DivideOperation()
        with pytest.raises(ValueError, match="Division by zero is not allowed"):
            operation.execute(x, y)

    def test_divide_operation_name(self):
        """Test operation name."""
        operation = DivideOperation()
        assert operation.name == "divide"
