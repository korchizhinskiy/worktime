from dishka.dependency_source.make_factory import provide  # type: ignore [reportUnknownVariableType]
from dishka.entities.scope import Scope
from dishka.provider import Provider

from app.auth.application.services.authentication import JWTService


class ServiceProvider(Provider):
    user_login_interactor = provide(
        JWTService,
        provides=JWTService,
        scope=Scope.REQUEST,
    )
