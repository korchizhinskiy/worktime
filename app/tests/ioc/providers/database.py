from dishka.dependency_source.make_context_var import from_context
from dishka.entities.scope import Scope
from dishka.provider import Provider
from sqlalchemy.ext.asyncio.session import AsyncSession


class SQLAlchemyProvider(Provider):
    session = from_context(provides=AsyncSession, scope=Scope.APP)
