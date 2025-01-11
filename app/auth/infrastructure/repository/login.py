from typing import override
from uuid import UUID

from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm.strategy_options import joinedload
from sqlalchemy.sql import select

from app.auth.application.dto.user import UserDTO
from app.auth.application.interfaces.repository.login import ILoginRepository
from app.user.infrastructure.models.user import User

type HashPassword = bytes
type UserId = UUID
type UserUsername = str


class LoginRepository(ILoginRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    @override
    async def get_user(self, username: UserUsername) -> UserDTO | None:
        user_query = select(User).options(joinedload(User.work_profile)).where(User.username == username)
        user = await self.session.scalar(user_query)

        if not user:
            return None

        return UserDTO.model_validate(user)
