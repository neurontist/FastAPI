from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import Config
from sqlmodel import SQLModel

engine = AsyncEngine(create_engine(
    url=Config.DATABASE_URL,
    echo=True
))

async def init_db():
    async with engine.begin() as conn:
        # statement = text("SELECT 'hello'")
        # result = await conn.execute(statement)
    
        # print(result.all())
        from src.books.models import Book
        await conn.run_sync(SQLModel.metadata.create_all)


