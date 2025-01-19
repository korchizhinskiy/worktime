from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm.strategy_options import joinedload
from sqlalchemy.sql import select

from app.auth.application.dto.profile import (
    AdministratorProfileDTO,
    AssistantManagerProfileDTO,
    ManagerProfileDTO,
    WorkProfileDTO,
)
from app.auth.application.exceptions.user import UserNotFoundError
from app.infrastructure.schemas.auth_user import AuthorizedUserDTO
from app.user.application.dto.user_profile import UserProfileDTO
from app.user.application.enums.roles import Role
from app.user.application.interfaces.query.user_profile import IUserProfileQuery
from app.user.infrastructure.models.user import User


class UserProfileQuery(IUserProfileQuery):
    """
    Get user's profile for current authenticated role.

    Use Case receives user role from auth token and return profile which depends on current user's role.
    """

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
            profile=self.get_profile_data(user, idp),
        )

    @staticmethod
    def get_profile_data(
        user: User,
        idp: AuthorizedUserDTO,
    ) -> WorkProfileDTO | ManagerProfileDTO | AssistantManagerProfileDTO | AdministratorProfileDTO:
        match idp.role:
            case Role.EMPLOYEE:
                return WorkProfileDTO(role=idp.role, specialization=user.work_profile.specialization)
            case Role.MANAGER:
                return ManagerProfileDTO(role=idp.role)
            case Role.ASSISTANT_MANAGER:
                return AssistantManagerProfileDTO(role=idp.role)
            case Role.ADMINISTRATOR:
                return AdministratorProfileDTO(role=idp.role)
