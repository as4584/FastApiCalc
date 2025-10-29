"""Dependency injection setup."""
from functools import lru_cache
from domain.services.calculator import CalculatorService
from domain.services.logger import StructuredLogger
from domain.operations.factory import OperationFactory
from domain.interfaces.logger import ILogger


@lru_cache()
def get_logger() -> ILogger:
    """Get singleton logger instance."""
    return StructuredLogger()


@lru_cache()
def get_operation_factory() -> OperationFactory:
    """Get singleton operation factory instance."""
    return OperationFactory()


def get_calculator_service(
    factory: OperationFactory = None,
    logger: ILogger = None,
) -> CalculatorService:
    """
    Get calculator service instance with dependencies.

    Args:
        factory: Operation factory (uses default if not provided)
        logger: Logger instance (uses default if not provided)

    Returns:
        CalculatorService instance
    """
    if factory is None:
        factory = get_operation_factory()
    if logger is None:
        logger = get_logger()

    return CalculatorService(factory, logger)
