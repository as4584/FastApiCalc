"""Arithmetic operations implementing Strategy pattern."""
from domain.operations.basic import (
    AddOperation,
    SubtractOperation,
    MultiplyOperation,
    DivideOperation,
)
from domain.operations.factory import OperationFactory

__all__ = [
    "AddOperation",
    "SubtractOperation",
    "MultiplyOperation",
    "DivideOperation",
    "OperationFactory",
]
