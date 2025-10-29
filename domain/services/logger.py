"""Structured logger implementation."""
import logging
import json
import sys
from datetime import datetime
from typing import Any
from domain.interfaces.logger import ILogger


class StructuredLogger(ILogger):
    """JSON-structured logger implementation."""

    def __init__(self, name: str = "fastapi_calculator"):
        """Initialize structured logger."""
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)

        # Remove existing handlers to avoid duplicates
        self.logger.handlers.clear()

        # Create console handler with JSON formatting
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.DEBUG)

        # Don't use the default formatter - we'll format in the methods
        self.logger.addHandler(handler)

        # Prevent propagation to avoid duplicate logs
        self.logger.propagate = False

    def _log(self, level: str, message: str, **kwargs: Any) -> None:
        """Internal method to format and log messages."""
        log_entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "level": level,
            "logger": "fastapi_calculator",
            "message": message,
            **kwargs,
        }

        # Print JSON to stdout
        print(json.dumps(log_entry), flush=True)

    def info(self, message: str, **kwargs: Any) -> None:
        """Log info level message."""
        self._log("INFO", message, **kwargs)

    def warning(self, message: str, **kwargs: Any) -> None:
        """Log warning level message."""
        self._log("WARNING", message, **kwargs)

    def error(self, message: str, **kwargs: Any) -> None:
        """Log error level message."""
        self._log("ERROR", message, **kwargs)

    def debug(self, message: str, **kwargs: Any) -> None:
        """Log debug level message."""
        self._log("DEBUG", message, **kwargs)
