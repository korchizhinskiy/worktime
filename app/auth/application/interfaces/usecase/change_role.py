from typing import Protocol

from app.auth.infrastructure.dependencies import AuthUserDTO
from app.user.application.enums.roles import Role


class UserChangeRoleUseCase(Protocol):
    async def execute(self, role: Role, idp: AuthUserDTO) -> None: ...
