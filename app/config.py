"""Configuration settings for the application."""

from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings."""

    # Server
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = False
    ENVIRONMENT: str = "production"
    LOG_LEVEL: str = "INFO"

    # API Keys
    OPENAI_API_KEY: str
    GOOGLE_SEARCH_API_KEY: Optional[str] = None
    PERPLEXITY_API_KEY: Optional[str] = None

    # Database
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/research_db"
    REDIS_URL: str = "redis://localhost:6379/0"

    # Agent Configuration
    NUM_AGENTS: int = 5
    AGENT_TIMEOUT: int = 30
    MAX_RETRIES: int = 3
    RETRY_DELAY: int = 2

    # Search Settings
    MAX_SEARCH_RESULTS: int = 20
    SEARCH_DEPTH: str = "comprehensive"
    INCLUDE_SOURCES: bool = True

    # Performance
    CACHE_TTL_MINUTES: int = 60
    MAX_CONCURRENT_REQUESTS: int = 1000
    BATCH_SIZE: int = 32

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()