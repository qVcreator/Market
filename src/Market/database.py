from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker
)

from .settings import settings

engine = create_async_engine(settings.DATABASE_URL, pool_pre_ping=True, future=True, echo=True)

async_session = async_sessionmaker(
    engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False
)


async def get_async_session() -> AsyncSession:
    session = async_session()
    try:
        yield session
    finally:
        await session.close()
