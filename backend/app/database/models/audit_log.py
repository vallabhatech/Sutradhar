from sqlalchemy import String, ForeignKey, Index
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base, TimestampMixin, UUIDMixin


class AuditLog(Base, UUIDMixin, TimestampMixin):
    """Audit log model for tracking user actions."""
    
    __tablename__ = "audit_logs"
    
    user_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )
    
    action: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )
    
    resource: Mapped[str] = mapped_column(
        String(255),
        nullable=True
    )
    
    details: Mapped[str] = mapped_column(
        String(1000),
        nullable=True
    )
    
    ip_address: Mapped[str] = mapped_column(
        String(45),
        nullable=True
    )
    
    user_agent: Mapped[str] = mapped_column(
        String(500),
        nullable=True
    )
    
    __table_args__ = (
        Index('idx_audit_user_action', 'user_id', 'action'),
        Index('idx_audit_timestamp', 'created_at'),
    )
    
    def __repr__(self) -> str:
        return f"<AuditLog(id={self.id}, user_id={self.user_id}, action={self.action})>"
