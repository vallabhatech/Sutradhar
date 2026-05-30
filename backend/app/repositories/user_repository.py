from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_
from typing import Optional, List
from app.database.models.user import User, UserRole
from app.schemas.user import UserCreate, UserUpdate


class UserRepository:
    """Repository for User model operations."""
    
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def create(self, user_data: UserCreate) -> User:
        """Create a new user."""
        from app.core.security import get_password_hash
        import uuid
        
        db_user = User(
            uuid=str(uuid.uuid4()),
            email=user_data.email,
            full_name=user_data.full_name,
            hashed_password=get_password_hash(user_data.password),
            role=user_data.role or UserRole.VIEWER.value,
            is_active=True,
            is_admin=False
        )
        
        self.db.add(db_user)
        await self.db.flush()
        await self.db.refresh(db_user)
        
        return db_user
    
    async def get_by_id(self, user_id: str) -> Optional[User]:
        """Get user by ID."""
        result = await self.db.execute(
            select(User).where(User.id == user_id)
        )
        return result.scalar_one_or_none()
    
    async def get_by_email(self, email: str) -> Optional[User]:
        """Get user by email."""
        result = await self.db.execute(
            select(User).where(User.email == email)
        )
        return result.scalar_one_or_none()
    
    async def get_by_uuid(self, uuid: str) -> Optional[User]:
        """Get user by UUID."""
        result = await self.db.execute(
            select(User).where(User.uuid == uuid)
        )
        return result.scalar_one_or_none()
    
    async def get_all(
        self,
        skip: int = 0,
        limit: int = 100,
        is_active: Optional[bool] = None,
        role: Optional[str] = None
    ) -> List[User]:
        """Get all users with optional filters."""
        query = select(User)
        
        conditions = []
        if is_active is not None:
            conditions.append(User.is_active == is_active)
        if role is not None:
            conditions.append(User.role == role)
        
        if conditions:
            query = query.where(and_(*conditions))
        
        query = query.offset(skip).limit(limit).order_by(User.created_at.desc())
        
        result = await self.db.execute(query)
        return result.scalars().all()
    
    async def update(self, user_id: str, user_data: UserUpdate) -> Optional[User]:
        """Update user information."""
        db_user = await self.get_by_id(user_id)
        
        if not db_user:
            return None
        
        update_data = user_data.model_dump(exclude_unset=True)
        
        for field, value in update_data.items():
            setattr(db_user, field, value)
        
        await self.db.flush()
        await self.db.refresh(db_user)
        
        return db_user
    
    async def delete(self, user_id: str) -> bool:
        """Delete user by ID."""
        db_user = await self.get_by_id(user_id)
        
        if not db_user:
            return False
        
        await self.db.delete(db_user)
        await self.db.flush()
        
        return True
    
    async def count(self, is_active: Optional[bool] = None) -> int:
        """Count users with optional filters."""
        from sqlalchemy import func
        
        query = select(func.count(User.id))
        
        if is_active is not None:
            query = query.where(User.is_active == is_active)
        
        result = await self.db.execute(query)
        return result.scalar()
