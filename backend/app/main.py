from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import SQLAlchemyError
from app.core.config import settings
from app.api.v1 import api_router
from app.middleware import (
    api_error_handler,
    validation_error_handler,
    sqlalchemy_error_handler,
    general_exception_handler
)
from app.core.logging_config import setup_logging
import logging

# Setup logging
setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Sutradhar API",
    description="AI-powered financial intelligence platform",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API router
app.include_router(api_router)

# Register exception handlers
app.add_exception_handler(Exception, general_exception_handler)
app.add_exception_handler(SQLAlchemyError, sqlalchemy_error_handler)
app.add_exception_handler(RequestValidationError, validation_error_handler)


@app.on_event("startup")
async def startup_event():
    """Run startup tasks."""
    logger.info("Starting Sutradhar API...")


@app.on_event("shutdown")
async def shutdown_event():
    """Run shutdown tasks."""
    logger.info("Shutting down Sutradhar API...")


@app.get("/health")
async def health_check():
    """
    Health check endpoint to verify service status.
    """
    return {
        "status": "healthy",
        "service": "sutradhar-api",
        "version": "1.0.0"
    }


@app.get("/")
async def root():
    """
    Root endpoint.
    """
    return {
        "message": "Sutradhar API",
        "version": "1.0.0",
        "docs": "/docs",
        "api_v1": "/api/v1"
    }
