"""FastAPI application entry point."""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from app.core.config import settings
from app.api.endpoints import calculator
from domain.models.response import HealthResponse

# Create FastAPI app
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="A calculator API with SOLID design principles",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Include routers
app.include_router(calculator.router, tags=["calculator"])

# Mount static files
static_path = Path(__file__).parent / "static"
if static_path.exists():
    app.mount("/static", StaticFiles(directory=str(static_path)), name="static")


@app.get("/", include_in_schema=False)
async def root():
    """Serve the calculator UI."""
    static_file = static_path / "index.html"
    if static_file.exists():
        return FileResponse(static_file)
    return {"message": "FastAPI Calculator API", "docs": "/docs"}


@app.get("/health", response_model=HealthResponse, tags=["health"])
async def health_check() -> HealthResponse:
    """Health check endpoint."""
    return HealthResponse(
        status="healthy",
        service="calculator",
        version=settings.app_version,
    )
