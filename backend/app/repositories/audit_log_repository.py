from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_
from typing import List, Optional
from datetime import datetime, timedelta
from app.database.models.audit_log import AuditLog
from app.schemas.audit_log import AuditLogCreate


class AuditLogRepository:
    """Repository for AuditLog model operations."""
    
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def create(self, audit_data: AuditLogCreate) -> AuditLog:
        """Create a new audit log entry."""
        db_audit = AuditLog(
            user_id=audit_data.user_id,
            action=audit_data.action,
            resource=audit_data.resource,
            details=audit_data.details,
            ip_address=audit_data.ip_address,
            user_agent=audit_data.user_agent
        )
        
        self.db.add(db_audit)
        await self.db.flush()
        await self.db.refresh(db_audit)
        
        return db_audit
    
    async def get_by_id(self, audit_id: str) -> Optional[AuditLog]:
        """Get audit log by ID."""
        result = await self.db.execute(
            select(AuditLog).where(AuditLog.id == audit_id)
        )
        return result.scalar_one_or_none()
    
    async def get_by_user(
        self,
        user_id: str,
        skip: int = 0,
        limit: int = 100,
        action: Optional[str] = None
    ) -> List[AuditLog]:
        """Get audit logs for a specific user."""
        query = select(AuditLog).where(AuditLog.user_id == user_id)
        
        if action:
            query = query.where(AuditLog.action == action)
        
        query = query.offset(skip).limit(limit).order_by(AuditLog.created_at.desc())
        
        result = await self.db.execute(query)
        return result.scalars().all()
    
    async def get_recent(
        self,
        hours: int = 24,
        skip: int = 0,
        limit: int = 100
    ) -> List[AuditLog]:
        """Get audit logs from the last N hours."""
        from datetime import datetime, timedelta
        
        cutoff_time = datetime.utcnow() - timedelta(hours=hours)
        
        query = select(AuditLog).where(
            AuditLog.created_at >= cutoff_time
        ).offset(skip).limit(limit).order_by(AuditLog.created_at.desc())
        
        result = await self.db.execute(query)
        return result.scalars().all()
