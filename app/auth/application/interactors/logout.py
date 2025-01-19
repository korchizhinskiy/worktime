from app.auth.application.interfaces.repository.logout import ILogoutRepository
from app.auth.application.interfaces.usecase.logout import UserLogoutUseCase
from app.infrastructure.schemas.auth_user import AuthorizedUserDTO


class UserLogoutInteractor(UserLogoutUseCase):
    def __init__(self, repository: ILogoutRepository) -> None:
        self.repository = repository

    async def execute(self, idp: AuthorizedUserDTO) -> None:
        await self.repository.delete_auth_session(idp.token)
