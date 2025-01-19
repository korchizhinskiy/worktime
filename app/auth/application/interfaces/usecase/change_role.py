from typing import Protocol

from app.infrastructure.schemas.auth_user import AuthorizedUserDTO
from app.user.application.enums.roles import Role


class UserChangeRoleUseCase(Protocol):
    async def execute(self, role: Role, idp: AuthorizedUserDTO) -> None: ...
