import os
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

from app.auth.infrastructure.models.base import Base as AuthBase
from app.infrastructure.config import Settings
from app.infrastructure.database import get_connection_url
from app.tests.ioc.dependencies import MockSettings
from app.training.infrastructure.models.base import Base as TrainingBase

config = context.config
# TODO: Temporary decision.
settings = Settings() if os.environ.get("PYTEST_VERSION") is None else MockSettings() # type: ignore [reportCallIssue]
config.set_main_option("sqlalchemy.url", f"{get_connection_url(settings)}?async_fallback=True")

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = [AuthBase.metadata, TrainingBase.metadata]


def run_migrations_offline() -> None:
    """
    Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """
    Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
