"""Response models."""
from pydantic import BaseModel, Field
from typing import Optional


class CalculationResponse(BaseModel):
    """Response model for calculation endpoint."""

    operation: str = Field(..., description="Operation performed")
    x: float = Field(..., description="First operand")
    y: float = Field(..., description="Second operand")
    result: float = Field(..., description="Calculation result")

    model_config = {
        "json_schema_extra": {
            "examples": [{"operation": "add", "x": 10, "y": 5, "result": 15}]
        }
    }


class ErrorResponse(BaseModel):
    """Response model for errors."""

    detail: str = Field(..., description="Error message")


class HealthResponse(BaseModel):
    """Response model for health check."""

    status: str = Field(default="healthy", description="Service status")
    service: str = Field(default="calculator", description="Service name")
    version: Optional[str] = Field(default="1.0.0", description="API version")
