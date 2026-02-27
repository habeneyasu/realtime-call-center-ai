"""
Configuration management for the application.

Centralizes environment variable loading and provides type-safe configuration.
"""

import os
from pathlib import Path
from typing import List
from pydantic_settings import BaseSettings
from dotenv import load_dotenv


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # Database
    db_host: str = "localhost"
    db_port: int = 5432
    db_user: str = "postgres"
    db_password: str = ""
    db_name: str = "andela_ai_engineering_bootcamp"
    
    # Redis
    redis_host: str = "localhost"
    redis_port: int = 6379
    redis_stream_name: str = "audio_chunks"
    
    # LLM Configuration
    use_ollama: bool = True
    use_huggingface: bool = False
    ollama_base_url: str = "http://localhost:11434/v1"
    huggingface_api_key: str = ""
    huggingface_endpoint: str = "https://api-inference.huggingface.co"
    llm_model: str = "llama3.2"
    llm_max_tokens: int = 1500
    llm_context_chunks: int = 8
    llm_analysis_interval: int = 10
    openrouter_api_key: str = ""
    openai_api_key: str = ""
    
    # API Configuration
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    
    # Security
    cors_origins: str = "*"
    api_key: str = ""
    rate_limit_per_minute: int = 60
    
    # Logging
    log_level: str = "INFO"
    log_format: str = "text"  # text or json
    
    # Environment
    environment: str = "development"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False
        
        @classmethod
        def parse_env_var(cls, field_name: str, raw_val: str) -> any:
            """Parse environment variables with type conversion."""
            if field_name in ["use_ollama", "use_huggingface"]:
                return raw_val.lower() in ("true", "1", "yes", "on")
            return raw_val


# Load .env from project root
project_root = Path(__file__).parent
env_path = project_root / '.env'
if env_path.exists():
    load_dotenv(dotenv_path=env_path, override=True)
else:
    load_dotenv(override=True)

# Create global settings instance
settings = Settings()

# Helper functions
def get_cors_origins() -> List[str]:
    """Get CORS origins as a list."""
    if settings.cors_origins == "*":
        return ["*"]
    return [origin.strip() for origin in settings.cors_origins.split(",")]


def is_production() -> bool:
    """Check if running in production environment."""
    return settings.environment.lower() == "production"


def is_development() -> bool:
    """Check if running in development environment."""
    return settings.environment.lower() == "development"
