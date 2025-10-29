"""Operation interface for Strategy pattern."""
from abc import ABC, abstractmethod


class IOperation(ABC):
    """Interface for arithmetic operations following Strategy pattern."""

    @abstractmethod
    def execute(self, x: float, y: float) -> float:
        """
        Execute the arithmetic operation.

        Args:
            x: First operand
            y: Second operand

        Returns:
            Result of the operation

        Raises:
            ValueError: If operation cannot be performed (e.g., division by zero)
        """
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        """Return the operation name."""
        pass
