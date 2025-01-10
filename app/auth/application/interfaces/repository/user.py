from typing import Protocol
from uuid import UUID

from app.auth.application.dto.registration import UserRegistrationDTO
from app.auth.application.dto.user import UserDTO

type HashPassword = bytes
type UserId = UUID
type UserUsername = str


class IUserRepository(Protocol):
    async def get_user(self, username: UserUsername) -> UserDTO | None: ...

    async def create(self, user_dto: UserRegistrationDTO) -> None: ...
