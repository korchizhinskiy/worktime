from typing import Protocol

from app.infrastructure.schemas.auth_user import AuthorizedUserDTO


class UserLogoutUseCase(Protocol):
    async def execute(self, idp: AuthorizedUserDTO) -> None: ...
