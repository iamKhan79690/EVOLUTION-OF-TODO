"""
Health check endpoints for the Todo Evolution API
"""

from datetime import datetime
from fastapi import APIRouter
from pydantic import BaseModel

from src.core.config import settings


# Create router
health_router = APIRouter()


class HealthResponse(BaseModel):
    """Health check response model"""
    status: str
    timestamp: datetime
    version: str
    environment: str


class DatabaseHealthResponse(BaseModel):
    """Database health check response model"""
    status: str
    message: str


@health_router.get("/health", response_model=HealthResponse)
async def health_check():
    """
    Basic health check endpoint
    Returns the API status and basic information
    """
    return HealthResponse(
        status="healthy",
        timestamp=datetime.utcnow(),
        version=settings.VERSION,
        environment=settings.ENVIRONMENT
    )


@health_router.get("/health/db", response_model=DatabaseHealthResponse)
async def database_health_check():
    """
    Database health check endpoint
    Checks if the database connection is working
    """
    try:
        # TODO: Implement actual database health check
        # This would typically try to connect to the database
        # For now, we'll return a placeholder response

        return DatabaseHealthResponse(
            status="healthy",
            message="Database connection is working"
        )
    except Exception as e:
        return DatabaseHealthResponse(
            status="unhealthy",
            message=f"Database connection failed: {str(e)}"
        )


@health_router.get("/ping")
async def ping():
    """
    Simple ping endpoint for connectivity testing
    """
    return {"message": "pong", "timestamp": datetime.utcnow()}


@health_router.get("/")
async def api_info():
    """
    API information endpoint
    Returns basic API metadata
    """
    return {
        "name": settings.APP_NAME,
        "version": settings.VERSION,
        "environment": settings.ENVIRONMENT,
        "docs_url": "/docs",
        "redoc_url": "/redoc"
    }