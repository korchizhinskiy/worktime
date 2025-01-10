from collections.abc import AsyncGenerator

import pytest
import pytest_asyncio
from alembic.command import downgrade, upgrade
from alembic.config import Config
from dishka.async_container import AsyncContainer, make_async_container
from dishka.integrations.fastapi import setup_dishka
from fastapi.applications import FastAPI
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio.engine import AsyncConnection, AsyncEngine, AsyncTransaction, create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession

from app.auth.presentation.api.routers.auth import router as auth_router
from app.auth.presentation.exceptions import setup_exception_handlers
from app.infrastructure.database import get_connection_url
from app.infrastructure.ioc.dependencies import Settings
from app.infrastructure.log_config import configure_logging
from app.tests.ioc.dependencies import MockSettings
from app.tests.ioc.providers import (
    ApplicationConfigProvider,
    AuthInteractorProvider,
    AuthRepositoryProvider,
    AuthServiceProvider,
    SQLAlchemyProvider,
    TrainingInteractorProvider,
    TrainingQueryProvider,
    TrainingRepositoryProvider,
    UserQueryProvider,
)
from app.training.presentation.api.routers import router as training_router
from app.user.presentation.api.routers.user_profile import router as user_router

pytest_plugins = ("app.tests.training.plugins.exercise",)


@pytest.fixture(autouse=True, scope="session")
async def setup_database(engine: AsyncEngine) -> AsyncGenerator[None]:
    config = Config("alembic.ini")
    async with engine.connect() as connection:
        await connection.run_sync(lambda _: upgrade(config, "head"))

    yield

    async with engine.connect() as connection:
        await connection.run_sync(lambda _: downgrade(config, "base"))


@pytest.fixture(scope="session")
def engine() -> AsyncEngine:
    database_url = get_connection_url(MockSettings())
    database_params = {}
    return create_async_engine(database_url, **database_params)


@pytest.fixture(scope="session")
async def connection(engine: AsyncEngine) -> AsyncGenerator[AsyncConnection, None]:
    async with engine.connect() as connection:
        yield connection


@pytest.fixture
async def transaction(
    connection: AsyncConnection,
) -> AsyncGenerator[AsyncTransaction, None]:
    async with connection.begin() as transaction:
        yield transaction


@pytest.fixture
async def session(
    connection: AsyncConnection,
    transaction: AsyncTransaction,
) -> AsyncGenerator[AsyncSession, None]:
    async_session = AsyncSession(
        bind=connection,
        join_transaction_mode="create_savepoint",
    )
    yield async_session

    await transaction.rollback()


@pytest_asyncio.fixture(scope="function", loop_scope="session")
async def client(
    session: AsyncSession,
) -> AsyncGenerator[AsyncClient]:
    # TODO: Set main router by package layer (in init module)

    container = make_async_container(
        ApplicationConfigProvider(),
        SQLAlchemyProvider(),
        AuthRepositoryProvider(),
        AuthInteractorProvider(),
        AuthServiceProvider(),
        UserQueryProvider(),
        TrainingQueryProvider(),
        TrainingRepositoryProvider(),
        TrainingInteractorProvider(),
        context={Settings: MockSettings(), AsyncSession: session},  # type: ignore [reportCallIssue]
    )
    app = FastAPI(swagger_ui_parameters={"persistAuthorization": True})

    app.include_router(auth_router)
    app.include_router(user_router)
    app.include_router(training_router)
    setup_exception_handlers(app)
    setup_dishka(container, app)
    configure_logging()
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://localhost:8000",
    ) as client:
        yield client
