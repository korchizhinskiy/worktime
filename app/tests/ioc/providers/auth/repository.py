from dishka.dependency_source.make_factory import provide  # type: ignore [reportUnknownVariableType]
from dishka.entities.scope import Scope
from dishka.provider import Provider

from app.auth.application.interfaces.repository.user import IUserRepository
from app.auth.infrastructure.repository.user import UserRepository


class RepositoryProvider(Provider):
    user_login_interactor = provide(
        UserRepository,
        provides=IUserRepository,
        scope=Scope.REQUEST,
    )
