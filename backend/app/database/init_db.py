from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import AsyncSessionLocal
from app.database.models import User, AuditLog
from app.database.base import Base
from app.core.security import get_password_hash


async def init_db():
    """
    Initialize database with tables and seed data.
    """
    async with AsyncSessionLocal() as session:
        async with session.begin():
            # Create all tables
            await session.run_sync(Base.metadata.create_all)
            
            # Check if admin user exists
            from sqlalchemy import select
            result = await session.execute(
                select(User).where(User.email == "admin@sutradhar.com")
            )
            admin_user = result.scalar_one_or_none()
            
            if not admin_user:
                # Create default admin user
                admin = User(
                    uuid="admin-uuid-001",
                    full_name="System Administrator",
                    email="admin@sutradhar.com",
                    hashed_password=get_password_hash("admin123"),
                    is_active=True,
                    is_admin=True,
                    role="ADMIN"
                )
                session.add(admin)
                await session.flush()
                
                # Create audit log for admin creation
                audit_log = AuditLog(
                    user_id=admin.id,
                    action="USER_CREATED",
                    resource="users",
                    details="Default admin user created during initialization"
                )
                session.add(audit_log)
            
            await session.commit()


if __name__ == "__main__":
    import asyncio
    asyncio.run(init_db())
