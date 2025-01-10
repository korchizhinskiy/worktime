from dishka.async_container import make_async_container
from dishka.integrations.fastapi import setup_dishka
from fastapi.applications import FastAPI
from pydantic_settings.main import BaseSettings, SettingsConfigDict

from app.infrastructure.config import CommonSettings, CryptoSettings, DatabaseConnectionSettings, Settings
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


class MockSettings(BaseSettings):
    certs: CryptoSettings
    db_connection: DatabaseConnectionSettings
    common: CommonSettings
    model_config = SettingsConfigDict(env_file=(".env.test",), env_nested_delimiter="__", str_to_lower=True)


def init_di(app: FastAPI) -> None:
    # Incompatible with pyright - in issue recomend change pyright to mypy
    # Issue: https://github.com/pydantic/pydantic-settings/issues/383
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
        context={Settings: MockSettings()},  # type: ignore [reportCallIssue]
    )
    setup_dishka(container, app)
