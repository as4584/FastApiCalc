"""Calculator API endpoints."""
from fastapi import APIRouter, HTTPException, Query
from domain.models.request import CalculationRequest
from domain.models.response import CalculationResponse
from app.core.dependencies import get_calculator_service

router = APIRouter()

# Get singleton calculator service
_calculator = get_calculator_service()


@router.get("/add", response_model=CalculationResponse)
async def add(
    x: float = Query(..., description="First number"),
    y: float = Query(..., description="Second number"),
) -> CalculationResponse:
    """Add two numbers."""
    try:
        result = _calculator.calculate("add", x, y)
        return CalculationResponse(operation="add", x=x, y=y, result=result)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/subtract", response_model=CalculationResponse)
async def subtract(
    x: float = Query(..., description="First number"),
    y: float = Query(..., description="Second number"),
) -> CalculationResponse:
    """Subtract y from x."""
    try:
        result = _calculator.calculate("subtract", x, y)
        return CalculationResponse(operation="subtract", x=x, y=y, result=result)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/multiply", response_model=CalculationResponse)
async def multiply(
    x: float = Query(..., description="First number"),
    y: float = Query(..., description="Second number"),
) -> CalculationResponse:
    """Multiply two numbers."""
    try:
        result = _calculator.calculate("multiply", x, y)
        return CalculationResponse(operation="multiply", x=x, y=y, result=result)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/divide", response_model=CalculationResponse)
async def divide(
    x: float = Query(..., description="First number"),
    y: float = Query(..., description="Second number"),
) -> CalculationResponse:
    """Divide x by y."""
    try:
        result = _calculator.calculate("divide", x, y)
        return CalculationResponse(operation="divide", x=x, y=y, result=result)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/calc", response_model=CalculationResponse)
async def calculate(
    request: CalculationRequest,
) -> CalculationResponse:
    """
    Perform calculation based on operation type.

    Supports: add, subtract, multiply, divide
    """
    try:
        result = _calculator.calculate(request.operation, request.x, request.y)
        return CalculationResponse(
            operation=request.operation,
            x=request.x,
            y=request.y,
            result=result,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
