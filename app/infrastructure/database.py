from app.infrastructure.config import Settings

type DBConnectionURL = str


def get_connection_url(settings: Settings) -> DBConnectionURL:
    return (
        f"postgresql+asyncpg://{settings.db_connection.database_user}:{settings.db_connection.database_password}@"
        f"{settings.db_connection.database_host}:{settings.db_connection.database_port}/{settings.db_connection.database_name}"
    )
