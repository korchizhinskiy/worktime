from uuid import UUID

from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.sql import select

from app.auth.application.dto.registration import UserRegistrationDTO
from app.auth.application.dto.user import UserDTO
from app.auth.application.interfaces.repository.user import IUserRepository
from app.auth.infrastructure.models.user import User

type HashPassword = bytes
type UserId = UUID
type UserUsername = str


class UserRepository(IUserRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_user(self, username: UserUsername) -> UserDTO | None:
        user_query = select(User).where(User.username == username)
        user = await self.session.scalar(user_query)

        if not user:
            return None

        return UserDTO.model_validate(user)

    async def create(self, user_dto: UserRegistrationDTO) -> None:
        user = User(**user_dto.model_dump())
        self.session.add(user)
        await self.session.commit()
