from fastapi import APIRouter

api_router = APIRouter()

# Health check endpoint
@api_router.get("/health")
async def health_check():
    """
    API health check endpoint.
    """
    return {
        "status": "healthy",
        "service": "sutradhar-api"
    }
