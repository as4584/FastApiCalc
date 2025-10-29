"""Interfaces for dependency inversion."""
from domain.interfaces.operations import IOperation
from domain.interfaces.logger import ILogger

__all__ = ["IOperation", "ILogger"]
