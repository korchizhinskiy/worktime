import time

import jwt
from sqlalchemy.ext.asyncio.session import AsyncSession

from app.auth.application.dto.user import AuthorizedUserDTO
from app.auth.infrastructure.models.session import AuthSession
from app.infrastructure.config import Settings
from app.user.application.enums.roles import Role

type AuthToken = bytes


class JWTService:
    def __init__(self, settings: Settings, session: AsyncSession) -> None:
        self.settings = settings
        self.session = session

    async def create_access_token(self, user_dto: AuthorizedUserDTO) -> str:
        sid = jwt.encode(
            payload={
                "sub": str(user_dto.id),
                # "exp": time.time() + 1000,
                # "crt": time.time(),
                # TODO: Add logic for change roles in system.
                "role": str(user_dto.role),
            },
            key=self.settings.certs.private_key,
            algorithm=self.settings.certs.algorithm,
        )
        self.session.add(AuthSession(token=sid, user_id=user_dto.id))
        await self.session.commit()
        return sid

    # TODO: Set in class, which work with authorization.
    # Functions:
    # - authenticate
    # - change_user_role
    async def change_user_role(self, token: AuthToken) -> str:
        # TODO: Add check for same role in request - return error, that user can not change role for the same.
        user_info = jwt.decode(token, key=self.settings.certs.public_key, algorithms=self.settings.certs.algorithm)
        sid = jwt.encode(
            payload={
                "sub": str(user_dto.id),
                # "exp": time.time() + 1000,
                # "crt": time.time(),
                # TODO: Add logic for change roles in system.
                "role": str(Role.EMPLOYEE),
            },
            key=self.settings.certs.private_key,
            algorithm=self.settings.certs.algorithm,
        )
        self.session.add(AuthSession(token=sid, user_id=user_dto.id))
        await self.session.commit()
        return sid
