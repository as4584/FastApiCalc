"""Request models."""
from pydantic import BaseModel, Field


class CalculationRequest(BaseModel):
    """Request model for calculation endpoint."""

    operation: str = Field(
        ...,
        description="Operation to perform (add, subtract, multiply, divide)",
        examples=["add"],
    )
    x: float = Field(..., description="First operand", examples=[10.0])
    y: float = Field(..., description="Second operand", examples=[5.0])

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"operation": "add", "x": 10, "y": 5},
                {"operation": "multiply", "x": 6, "y": 7},
            ]
        }
    }
