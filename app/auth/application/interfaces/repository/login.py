from typing import Protocol
from uuid import UUID

from app.auth.application.dto.user import UserDTO

type HashPassword = bytes
type UserId = UUID
type UserUsername = str


class ILoginRepository(Protocol):
    async def get_user(self, username: UserUsername) -> UserDTO | None: ...
