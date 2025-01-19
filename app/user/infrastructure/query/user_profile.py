from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm.strategy_options import joinedload
from sqlalchemy.sql import select

from app.auth.application.exceptions.user import UserNotFoundError
from app.infrastructure.schemas.auth_user import AuthorizedUserDTO
from app.user.application.dto.user_profile import UserProfileDTO
from app.user.application.enums.roles import Role
from app.user.application.interfaces.query.user_profile import IUserProfileQuery
from app.user.infrastructure.models.user import User


class UserProfileQuery(IUserProfileQuery):
    # TODO: Add role into output

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def execute(self, idp: AuthorizedUserDTO) -> UserProfileDTO:
        match idp.role:
            case Role.EMPLOYEE:
                profile_load = joinedload(User.work_profile)
            case Role.MANAGER:
                profile_load = joinedload(User.manager_profile)
            case Role.ASSISTANT_MANAGER:
                profile_load = joinedload(User.assistant_manager_profile)
            case Role.ADMINISTRATOR:
                profile_load = joinedload(User.administrator_profile)

        query = select(User).where(User.id == idp.id).options(profile_load)

        user = await self.session.scalar(query)

        # WARN: This situation in 99% is unreal.
        if not user:
            raise UserNotFoundError(username=idp.username)

        return UserProfileDTO(
            id=user.id,
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            second_name=user.second_name,
            role=idp.role,
        )
