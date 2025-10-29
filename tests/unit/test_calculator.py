"""Unit tests for operation factory and calculator service."""
import pytest
from domain.operations.factory import OperationFactory
from domain.operations.basic import AddOperation, SubtractOperation
from domain.services.calculator import CalculatorService
from domain.services.logger import StructuredLogger


class TestOperationFactory:
    """Test cases for OperationFactory."""

    def test_get_add_operation(self):
        """Test getting add operation."""
        factory = OperationFactory()
        operation = factory.get_operation("add")
        assert operation.name == "add"
        assert operation.execute(5, 3) == 8

    def test_get_subtract_operation(self):
        """Test getting subtract operation."""
        factory = OperationFactory()
        operation = factory.get_operation("subtract")
        assert operation.name == "subtract"
        assert operation.execute(10, 3) == 7

    def test_get_multiply_operation(self):
        """Test getting multiply operation."""
        factory = OperationFactory()
        operation = factory.get_operation("multiply")
        assert operation.name == "multiply"
        assert operation.execute(5, 3) == 15

    def test_get_divide_operation(self):
        """Test getting divide operation."""
        factory = OperationFactory()
        operation = factory.get_operation("divide")
        assert operation.name == "divide"
        assert operation.execute(10, 2) == 5.0

    def test_invalid_operation_raises_error(self):
        """Test that invalid operation name raises ValueError."""
        factory = OperationFactory()
        with pytest.raises(ValueError, match="Invalid operation: power"):
            factory.get_operation("power")

    def test_case_insensitive_operation_name(self):
        """Test that operation names are case-insensitive."""
        factory = OperationFactory()
        operation = factory.get_operation("ADD")
        assert operation.name == "add"

    def test_get_available_operations(self):
        """Test getting list of available operations."""
        factory = OperationFactory()
        operations = factory.get_available_operations()
        assert "add" in operations
        assert "subtract" in operations
        assert "multiply" in operations
        assert "divide" in operations
        assert len(operations) == 4


class TestCalculatorService:
    """Test cases for CalculatorService."""

    @pytest.fixture
    def calculator_service(self):
        """Create calculator service instance."""
        factory = OperationFactory()
        logger = StructuredLogger()
        return CalculatorService(factory, logger)

    def test_calculate_add(self, calculator_service):
        """Test calculate method with add operation."""
        result = calculator_service.calculate("add", 10, 5)
        assert result == 15

    def test_calculate_subtract(self, calculator_service):
        """Test calculate method with subtract operation."""
        result = calculator_service.calculate("subtract", 10, 5)
        assert result == 5

    def test_calculate_multiply(self, calculator_service):
        """Test calculate method with multiply operation."""
        result = calculator_service.calculate("multiply", 6, 7)
        assert result == 42

    def test_calculate_divide(self, calculator_service):
        """Test calculate method with divide operation."""
        result = calculator_service.calculate("divide", 20, 4)
        assert result == 5.0

    def test_calculate_divide_by_zero(self, calculator_service):
        """Test that divide by zero raises ValueError."""
        with pytest.raises(ValueError, match="Division by zero is not allowed"):
            calculator_service.calculate("divide", 10, 0)

    def test_calculate_invalid_operation(self, calculator_service):
        """Test that invalid operation raises ValueError."""
        with pytest.raises(ValueError, match="Invalid operation"):
            calculator_service.calculate("modulo", 10, 3)

    def test_get_available_operations(self, calculator_service):
        """Test getting available operations from service."""
        operations = calculator_service.get_available_operations()
        assert len(operations) == 4
        assert "add" in operations
