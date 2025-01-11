from dishka.dependency_source.make_factory import provide  # type: ignore [reportUnknownVariableType]
from dishka.entities.scope import Scope
from dishka.provider import Provider

from app.auth.application.interfaces.repository.login import ILoginRepository
from app.auth.application.interfaces.repository.logout import ILogoutRepository
from app.auth.application.interfaces.repository.registration import IRegistrationRepository
from app.auth.infrastructure.repository.login import LoginRepository
from app.auth.infrastructure.repository.logout import LogoutRepository
from app.auth.infrastructure.repository.registration import RegistrationRepository


class RepositoryProvider(Provider):
    scope = Scope.REQUEST

    user_repository = provide(RegistrationRepository, provides=IRegistrationRepository)
    user_login_repository = provide(LoginRepository, provides=ILoginRepository)
    user_logout_repository = provide(LogoutRepository, provides=ILogoutRepository)
