"""Calculator service orchestrating operations."""
from domain.interfaces.operations import IOperation
from domain.interfaces.logger import ILogger
from domain.operations.factory import OperationFactory


class CalculatorService:
    """Service to perform calculations using operation strategies."""

    def __init__(self, operation_factory: OperationFactory, logger: ILogger):
        """
        Initialize calculator service.

        Args:
            operation_factory: Factory to resolve operations
            logger: Logger for structured logging
        """
        self._factory = operation_factory
        self._logger = logger

    def calculate(self, operation_name: str, x: float, y: float) -> float:
        """
        Perform calculation.

        Args:
            operation_name: Name of operation to perform
            x: First operand
            y: Second operand

        Returns:
            Calculation result

        Raises:
            ValueError: If operation is invalid or execution fails
        """
        self._logger.info(
            "Calculation requested",
            operation=operation_name,
            x=x,
            y=y,
        )

        try:
            operation = self._factory.get_operation(operation_name)
            result = operation.execute(x, y)

            self._logger.info(
                "Calculation completed",
                operation=operation_name,
                x=x,
                y=y,
                result=result,
            )

            return result

        except ValueError as e:
            self._logger.error(
                "Calculation failed",
                operation=operation_name,
                x=x,
                y=y,
                error=str(e),
            )
            raise

    def get_available_operations(self) -> list[str]:
        """Return list of available operations."""
        return self._factory.get_available_operations()
