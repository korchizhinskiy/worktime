from typing import Protocol

from app.auth.application.dto.registration import UserRegistrationDTO


class UserRegistrationUseCase(Protocol):
    async def execute(self, user_dto: UserRegistrationDTO) -> None: ...
