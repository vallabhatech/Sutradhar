from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Optional


class AuditLogBase(BaseModel):
    """Base audit log schema."""
    action: str = Field(..., max_length=100)
    resource: Optional[str] = Field(None, max_length=255)
    details: Optional[str] = Field(None, max_length=1000)


class AuditLogCreate(AuditLogBase):
    """Schema for creating audit log."""
    user_id: str
    ip_address: Optional[str] = Field(None, max_length=45)
    user_agent: Optional[str] = Field(None, max_length=500)


class AuditLogResponse(BaseModel):
    """Schema for audit log response."""
    model_config = ConfigDict(from_attributes=True)
    
    id: str
    user_id: str
    action: str
    resource: Optional[str]
    details: Optional[str]
    ip_address: Optional[str]
    user_agent: Optional[str]
    created_at: datetime
    updated_at: datetime
