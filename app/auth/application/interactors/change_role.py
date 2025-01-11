from logging import getLogger
from typing import final

from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.sql.expression import exists, select

from app.auth.application.services.authentication import JWTService
from app.auth.infrastructure.dependencies import AuthUserDTO
from app.user.application.enums.roles import Role
from app.user.infrastructure.models.work_profile import WorkProfile

log = getLogger(__name__)


@final
class UserChangeRoleInteractor:
    def __init__(self, auth_service: JWTService, session: AsyncSession) -> None:
        self.auth_service = auth_service
        self.session = session

    async def execute(self, role: Role, idp: AuthUserDTO) -> None | str:
        if role == Role.EMPLOYEE:
            is_exist_query = select(exists().where(WorkProfile.user_id == idp.id))
            is_work_profile_exist = await self.session.scalar(is_exist_query)
            if is_work_profile_exist:
                idp.role = Role.EMPLOYEE
                return await self.auth_service.create_access_token(idp)
        return None
