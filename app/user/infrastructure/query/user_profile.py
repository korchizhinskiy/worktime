from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.sql import select

from app.auth.application.dto.user import UserDTO
from app.user.application.dto.user_profile import UserProfileDTO
from app.user.application.interfaces.query.user_profile import IUserProfileQuery
from app.user.infrastructure.models.user import User


class UserProfileQuery(IUserProfileQuery):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def execute(self, idp: UserDTO) -> UserProfileDTO:
        query = select(User).where(User.id == idp.id)

        user = await self.session.scalar(query)
        return UserProfileDTO.model_validate(user)
