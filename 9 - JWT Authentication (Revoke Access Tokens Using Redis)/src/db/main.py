from sqlalchemy.ext.asyncio import create_async_engine
from src.config import Config
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import AsyncGenerator
from sqlalchemy.orm import sessionmaker

# Use SQLAlchemy's async engine. The previous code wrapped a sync engine
# which can block async calls and cause requests to hang.
engine = create_async_engine(
    Config.DATABASE_URL,
    echo=True,
)

# Create a session factory bound to the async engine
SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

async def init_db():
    async with engine.begin() as conn:
        # Import models to ensure they're registered on SQLModel.metadata
        from src.books.models import Book  # noqa: F401
        from src.auth.models import User  # noqa: F401
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session
