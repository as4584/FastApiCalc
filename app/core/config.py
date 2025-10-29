"""Application configuration."""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    app_name: str = "FastAPI Calculator"
    app_version: str = "1.0.0"
    debug: bool = False

    model_config = {
        "env_file": ".env",
        "case_sensitive": False,
    }


settings = Settings()
