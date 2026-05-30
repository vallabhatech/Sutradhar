from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_db
from app.services.auth_service import AuthService
from app.schemas.user import UserCreate, UserLogin, Token
from app.api.v1.auth.dependencies import get_current_user, get_current_active_user

router = APIRouter()


@router.post("/register", response_model=Token, status_code=status.HTTP_201_CREATED)
async def register(
    user_data: UserCreate,
    request: Request,
    db: AsyncSession = Depends(get_db)
):
    """
    Register a new user.
    
    - **email**: User email (must be unique)
    - **password**: User password (min 8 characters)
    - **full_name**: User full name
    - **role**: User role (default: VIEWER)
    """
    try:
        auth_service = AuthService(db)
        
        # Get client info
        ip_address = request.client.host if request.client else None
        user_agent = request.headers.get("user-agent")
        
        token = await auth_service.register(
            user_data=user_data,
            ip_address=ip_address,
            user_agent=user_agent
        )
        
        return token
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.post("/login", response_model=Token)
async def login(
    login_data: UserLogin,
    request: Request,
    db: AsyncSession = Depends(get_db)
):
    """
    Login user with email and password.
    
    - **email**: User email
    - **password**: User password
    """
    try:
        auth_service = AuthService(db)
        
        # Get client info
        ip_address = request.client.host if request.client else None
        user_agent = request.headers.get("user-agent")
        
        token = await auth_service.login(
            login_data=login_data,
            ip_address=ip_address,
            user_agent=user_agent
        )
        
        return token
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
            headers={"WWW-Authenticate": "Bearer"},
        )


@router.get("/me")
async def get_me(
    current_user = Depends(get_current_active_user)
):
    """
    Get current authenticated user information.
    """
    return current_user
