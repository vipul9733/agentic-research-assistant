"""Main FastAPI application for Agentic Research Assistant."""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging

from app.config import settings
from app.api.routes import router

# Configure logging
logging.basicConfig(level=settings.LOG_LEVEL)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application startup and shutdown."""
    logger.info("Starting Agentic Research Assistant")
    yield
    logger.info("Shutting down Agentic Research Assistant")


app = FastAPI(
    title="Agentic Research Assistant",
    description="Production-Grade Multi-Agent System for Autonomous Research",
    version="1.0.0",
    lifespan=lifespan,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(router, prefix="/api/v1")


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "agentic-research-assistant"}


@app.get("/ready")
async def readiness_check():
    """Readiness check endpoint."""
    return {"status": "ready", "service": "agentic-research-assistant"}


@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "name": "Agentic Research Assistant",
        "version": "1.0.0",
        "docs": "/docs",
        "endpoints": {
            "research": "/api/v1/research",
            "status": "/api/v1/research/{research_id}/status",
            "health": "/health",
            "ready": "/ready",
        },
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host=settings.HOST,
        port=settings.PORT,
        log_level=settings.LOG_LEVEL.lower(),
    )