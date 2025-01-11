from dishka.dependency_source.make_factory import provide  # type: ignore [reportUnknownVariableType]
from dishka.entities.scope import Scope
from dishka.provider import Provider

from app.auth.application.interactors.change_role import UserChangeRoleInteractor
from app.auth.application.interactors.logout import UserLogoutInteractor
from app.auth.application.interactors.user_login import UserLoginInteractor
from app.auth.application.interactors.user_registration import UserRegistrationInteractor
from app.auth.application.interfaces.usecase.change_role import UserChangeRoleUseCase
from app.auth.application.interfaces.usecase.logout import UserLogoutUseCase
from app.auth.application.interfaces.usecase.user_login import UserLoginUseCase
from app.auth.application.interfaces.usecase.user_registration import UserRegistrationUseCase


class InteractorProvider(Provider):
    user_registration_interactor = provide(
        UserLoginInteractor,
        provides=UserLoginUseCase,
        scope=Scope.REQUEST,
    )
    user_login_interactor = provide(
        UserRegistrationInteractor,
        provides=UserRegistrationUseCase,
        scope=Scope.REQUEST,
    )
    user_logout_interactor = provide(
        UserLogoutInteractor,
        provides=UserLogoutUseCase,
        scope=Scope.REQUEST,
    )
    user_change_role_interactor = provide(
        UserChangeRoleInteractor,
        provides=UserChangeRoleUseCase,
        scope=Scope.REQUEST,
    )
