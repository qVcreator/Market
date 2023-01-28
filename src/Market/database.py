from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_session
from sqlalchemy.orm import sessionmaker, Session

from .settings import settings

engine = create_async_engine(settings.DATABASE_URL, pool_pre_ping=True, future=True, echo=True)

Session = sessionmaker(
    engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession
)
