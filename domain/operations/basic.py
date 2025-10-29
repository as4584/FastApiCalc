"""Concrete implementations of arithmetic operations."""
from domain.interfaces.operations import IOperation


class AddOperation(IOperation):
    """Addition operation strategy."""

    @property
    def name(self) -> str:
        return "add"

    def execute(self, x: float, y: float) -> float:
        """Add two numbers."""
        return x + y


class SubtractOperation(IOperation):
    """Subtraction operation strategy."""

    @property
    def name(self) -> str:
        return "subtract"

    def execute(self, x: float, y: float) -> float:
        """Subtract y from x."""
        return x - y


class MultiplyOperation(IOperation):
    """Multiplication operation strategy."""

    @property
    def name(self) -> str:
        return "multiply"

    def execute(self, x: float, y: float) -> float:
        """Multiply two numbers."""
        return x * y


class DivideOperation(IOperation):
    """Division operation strategy."""

    @property
    def name(self) -> str:
        return "divide"

    def execute(self, x: float, y: float) -> float:
        """
        Divide x by y.

        Raises:
            ValueError: If y is zero
        """
        if y == 0:
            raise ValueError("Division by zero is not allowed")
        return x / y
