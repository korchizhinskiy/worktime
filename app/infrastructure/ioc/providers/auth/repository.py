from dishka.dependency_source.make_factory import provide  # type: ignore [reportUnknownVariableType]
from dishka.entities.scope import Scope
from dishka.provider import Provider

from app.auth.application.interfaces.repository.login import ILoginRepository
from app.auth.application.interfaces.repository.user import IUserRepository
from app.auth.infrastructure.repository.login import LoginRepository
from app.auth.infrastructure.repository.user import UserRepository


class RepositoryProvider(Provider):
    scope = Scope.REQUEST

    user_repository = provide(UserRepository, provides=IUserRepository)
    user_login_repository = provide(LoginRepository, provides=ILoginRepository)
