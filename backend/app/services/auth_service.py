from sqlalchemy.ext.asyncio import AsyncSession
from datetime import timedelta
from typing import Optional
from app.repositories.user_repository import UserRepository
from app.repositories.audit_log_repository import AuditLogRepository
from app.schemas.user import UserCreate, UserLogin, Token, UserResponse
from app.core.security import verify_password, create_access_token
from app.core.config import settings


class AuthService:
    """Service for authentication operations."""
    
    def __init__(self, db: AsyncSession):
        self.db = db
        self.user_repo = UserRepository(db)
        self.audit_repo = AuditLogRepository(db)
    
    async def register(
        self,
        user_data: UserCreate,
        ip_address: Optional[str] = None,
        user_agent: Optional[str] = None
    ) -> Token:
        """Register a new user."""
        # Check if user already exists
        existing_user = await self.user_repo.get_by_email(user_data.email)
        if existing_user:
            raise ValueError("Email already registered")
        
        # Create new user
        user = await self.user_repo.create(user_data)
        
        # Create audit log
        await self.audit_repo.create(
            AuditLogCreate(
                user_id=user.id,
                action="USER_REGISTERED",
                resource="users",
                details=f"User registered with email: {user.email}",
                ip_address=ip_address,
                user_agent=user_agent
            )
        )
        
        # Generate access token
        access_token = create_access_token(
            data={"sub": user.id, "role": user.role},
            expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        )
        
        return Token(
            access_token=access_token,
            user=UserResponse.model_validate(user)
        )
    
    async def login(
        self,
        login_data: UserLogin,
        ip_address: Optional[str] = None,
        user_agent: Optional[str] = None
    ) -> Token:
        """Login user with email and password."""
        # Get user by email
        user = await self.user_repo.get_by_email(login_data.email)
        
        if not user:
            raise ValueError("Invalid credentials")
        
        # Verify password
        if not verify_password(login_data.password, user.hashed_password):
            raise ValueError("Invalid credentials")
        
        # Check if user is active
        if not user.is_active:
            raise ValueError("Account is inactive")
        
        # Create audit log
        await self.audit_repo.create(
            AuditLogCreate(
                user_id=user.id,
                action="USER_LOGIN",
                resource="auth",
                details=f"User logged in with email: {user.email}",
                ip_address=ip_address,
                user_agent=user_agent
            )
        )
        
        # Generate access token
        access_token = create_access_token(
            data={"sub": user.id, "role": user.role},
            expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        )
        
        return Token(
            access_token=access_token,
            user=UserResponse.model_validate(user)
        )
    
    async def get_current_user(self, user_id: str) -> UserResponse:
        """Get current user by ID."""
        user = await self.user_repo.get_by_id(user_id)
        
        if not user:
            raise ValueError("User not found")
        
        if not user.is_active:
            raise ValueError("Account is inactive")
        
        return UserResponse.model_validate(user)
