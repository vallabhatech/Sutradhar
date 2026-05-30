from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health_check():
    """
    System health check endpoint.
    """
    return {
        "status": "healthy",
        "service": "sutradhar-api",
        "version": "1.0.0"
    }


@router.get("/info")
async def system_info():
    """
    System information endpoint.
    """
    return {
        "name": "Sutradhar",
        "description": "AI-powered financial intelligence platform",
        "version": "1.0.0",
        "status": "operational"
    }
