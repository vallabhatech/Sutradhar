from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
from app.database.session import get_db
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserResponse, UserUpdate
from app.api.v1.auth.dependencies import get_current_active_user, require_admin

router = APIRouter()


@router.get("", response_model=list[UserResponse])
async def get_users(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    is_active: Optional[bool] = None,
    role: Optional[str] = None,
    current_user = Depends(require_admin),
    db: AsyncSession = Depends(get_db)
):
    """
    Get all users (admin only).
    
    - **skip**: Number of users to skip
    - **limit**: Maximum number of users to return
    - **is_active**: Filter by active status
    - **role**: Filter by role
    """
    user_repo = UserRepository(db)
    users = await user_repo.get_all(
        skip=skip,
        limit=limit,
        is_active=is_active,
        role=role
    )
    return [UserResponse.model_validate(user) for user in users]


@router.get("/me", response_model=UserResponse)
async def get_current_user_details(
    current_user = Depends(get_current_active_user)
):
    """
    Get current user details.
    """
    return current_user


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: str,
    current_user = Depends(require_admin),
    db: AsyncSession = Depends(get_db)
):
    """
    Get user by ID (admin only).
    """
    user_repo = UserRepository(db)
    user = await user_repo.get_by_id(user_id)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return UserResponse.model_validate(user)


@router.patch("/{user_id}", response_model=UserResponse)
async def update_user(
    user_id: str,
    user_data: UserUpdate,
    current_user = Depends(require_admin),
    db: AsyncSession = Depends(get_db)
):
    """
    Update user information (admin only).
    """
    user_repo = UserRepository(db)
    user = await user_repo.update(user_id, user_data)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return UserResponse.model_validate(user)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: str,
    current_user = Depends(require_admin),
    db: AsyncSession = Depends(get_db)
):
    """
    Delete user (admin only).
    """
    user_repo = UserRepository(db)
    success = await user_repo.delete(user_id)
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
