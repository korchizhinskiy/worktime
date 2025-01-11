from typing import Protocol

from app.auth.infrastructure.dependencies import AuthUserDTO


class UserLogoutUseCase(Protocol):
    async def execute(self, idp: AuthUserDTO) -> None: ...
