from typing import Protocol

from app.auth.application.dto.user import UserDTO
from app.user.application.enums.roles import Role


class UserChangeRoleUseCase(Protocol):
    async def execute(self, role: Role, idp: UserDTO) -> None: ...
