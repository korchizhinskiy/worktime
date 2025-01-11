from app.auth.application.dto.user import UserDTO
from app.auth.application.interfaces.repository.logout import ILogoutRepository
from app.auth.application.interfaces.usecase.logout import UserLogoutUseCase
from app.auth.infrastructure.dependencies import AuthUserDTO


class UserLogoutInteractor(UserLogoutUseCase):
    def __init__(self, repository: ILogoutRepository) -> None:
        self.repository = repository

    async def execute(self, idp: AuthUserDTO) -> None:
        await self.repository.delete_auth_session(idp.token)
