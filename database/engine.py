import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from database.models import Base 


engine = create_async_engine(os.getenv('DB_LITE'), echo=True)

session_maker = async_sessionmaker(bind = engine, class_=AsyncSession, expire_on_commit=False)


async def create_db() -> None: 
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        

async def drop_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)