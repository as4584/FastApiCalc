"""Logger interface for dependency inversion."""
from abc import ABC, abstractmethod
from typing import Any, Dict


class ILogger(ABC):
    """Interface for structured logging."""

    @abstractmethod
    def info(self, message: str, **kwargs: Any) -> None:
        """Log info level message with context."""
        pass

    @abstractmethod
    def warning(self, message: str, **kwargs: Any) -> None:
        """Log warning level message with context."""
        pass

    @abstractmethod
    def error(self, message: str, **kwargs: Any) -> None:
        """Log error level message with context."""
        pass

    @abstractmethod
    def debug(self, message: str, **kwargs: Any) -> None:
        """Log debug level message with context."""
        pass
