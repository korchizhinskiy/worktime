from typing import Protocol

from app.auth.application.dto.login import UserLoginDTO
from app.auth.application.dto.user_token import TokenDTO


class UserLoginUseCase(Protocol):
    async def execute(self, user_dto: UserLoginDTO) -> TokenDTO: ...
