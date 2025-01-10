from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.sql import select

from app.auth.application.dto.user import UserDTO
from app.auth.infrastructure.models.user import User
from app.user.application.dto.user_profile import UserProfileDTO
from app.user.application.interfaces.query.user_profile import IUserProfileQuery


class UserProfileQuery(IUserProfileQuery):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def execute(self, idp: UserDTO) -> UserProfileDTO:
        query = select(User).where(User.id == idp.id)

        user = await self.session.scalar(query)
        return UserProfileDTO.model_validate(user)
