from collections.abc import AsyncGenerator

from dishka.dependency_source.make_factory import provide  # type: ignore [reportUnknownVariableType]
from dishka.entities.scope import Scope
from dishka.provider import Provider
from sqlalchemy.ext.asyncio.engine import AsyncEngine, create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession, async_sessionmaker

from app.infrastructure.config import Settings
from app.infrastructure.database import get_connection_url


class SQLAlchemyProvider(Provider):
    @classmethod
    @provide(scope=Scope.APP)
    async def get_engine(cls, settings: Settings) -> AsyncEngine:
        database_url = get_connection_url(settings)
        database_params = {}
        return create_async_engine(database_url, **database_params)

    @classmethod
    @provide(scope=Scope.REQUEST)
    async def get_session(cls, engine: AsyncEngine) -> AsyncGenerator[AsyncSession, None]:
        async_session = async_sessionmaker(
            engine,
            class_=AsyncSession,
            expire_on_commit=False,
            autoflush=False,
        )
        async with async_session() as session:
            yield session
