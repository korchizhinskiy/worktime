from typing import override
from uuid import UUID

from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm.strategy_options import joinedload
from sqlalchemy.sql import select

from app.auth.application.dto.registration import UserRegistrationDTO
from app.auth.application.dto.user import UserDTO
from app.auth.application.interfaces.repository.registration import IRegistrationRepository
from app.user.application.enums.roles import Role
from app.user.infrastructure.models.administrator_profile import AdministratorProfile
from app.user.infrastructure.models.assistant_manager_profile import AssistantManagerProfile
from app.user.infrastructure.models.manager_profile import ManagerProfile
from app.user.infrastructure.models.user import User
from app.user.infrastructure.models.work_profile import WorkProfile

type HashPassword = bytes
type UserId = UUID
type UserUsername = str


class RegistrationRepository(IRegistrationRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    @override
    async def get_user(self, username: UserUsername) -> UserDTO | None:
        user_query = select(User).options(joinedload(User.work_profile)).where(User.username == username)
        user = await self.session.scalar(user_query)

        if not user:
            return None

        return UserDTO.model_validate(user)

    @override
    async def create(self, user_dto: UserRegistrationDTO) -> None:
        # TODO: Explicitly list attributes on creation User object.
        user = User(**user_dto.model_dump(exclude={"profile"}))
        match user_dto.profile.role:
            case Role.EMPLOYEE:
                profile = WorkProfile(user=user, specialization=user_dto.profile.specialization)
            case Role.MANAGER:
                profile = ManagerProfile(user=user)
            case Role.ASSISTANT_MANAGER:
                profile = AssistantManagerProfile(user=user)
            case Role.ADMINISTRATOR:
                profile = AdministratorProfile(user=user)
        self.session.add(user)
        self.session.add(profile)
        await self.session.commit()
