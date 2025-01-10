from dishka.dependency_source import from_context
from dishka.entities.scope import Scope
from dishka.provider import Provider

from app.infrastructure.ioc.dependencies import Settings


class ApplicationConfigProvider(Provider):
    config = from_context(provides=Settings, scope=Scope.APP)
