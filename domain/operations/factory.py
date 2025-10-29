"""Factory for resolving operations by name."""
from typing import Dict
from domain.interfaces.operations import IOperation
from domain.operations.basic import (
    AddOperation,
    SubtractOperation,
    MultiplyOperation,
    DivideOperation,
)


class OperationFactory:
    """Factory to resolve operation strategies by name."""

    def __init__(self):
        """Initialize factory with available operations."""
        self._operations: Dict[str, IOperation] = {
            "add": AddOperation(),
            "subtract": SubtractOperation(),
            "multiply": MultiplyOperation(),
            "divide": DivideOperation(),
        }

    def get_operation(self, name: str) -> IOperation:
        """
        Get operation by name.

        Args:
            name: Operation name (add, subtract, multiply, divide)

        Returns:
            Operation instance

        Raises:
            ValueError: If operation name is not supported
        """
        operation = self._operations.get(name.lower())
        if operation is None:
            raise ValueError(
                f"Invalid operation: {name}. "
                f"Supported operations: {', '.join(self._operations.keys())}"
            )
        return operation

    def get_available_operations(self) -> list[str]:
        """Return list of available operation names."""
        return list(self._operations.keys())
