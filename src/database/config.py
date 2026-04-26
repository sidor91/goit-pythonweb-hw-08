import os
from dotenv import load_dotenv

import contextlib

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    async_sessionmaker,
    create_async_engine,
)

load_dotenv()

url_to_db = os.getenv("DATABASE_URL")

class DatabaseSessionManager:
    def __init__(self, url: str):
        self._engine: AsyncEngine | None = create_async_engine(url)
        self._session_maker = async_sessionmaker(
            autoflush=False, autocommit=False, bind=self._engine
        )

    @contextlib.asynccontextmanager
    async def session(self):
        session = self._session_maker()
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

if (url_to_db is None):
    raise Exception("Database URL is not set")
sessionmanager = DatabaseSessionManager(url_to_db)


async def get_db():
    async with sessionmanager.session() as session:
        yield session
