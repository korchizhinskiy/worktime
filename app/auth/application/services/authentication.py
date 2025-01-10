import json
import time

import jwt
from sqlalchemy.ext.asyncio.session import AsyncSession

from app.auth.application.dto.user import UserDTO
from app.auth.infrastructure.models.session import AuthSession
from app.infrastructure.config import Settings
from app.user.application.enums.roles import Role


class JWTService:
    def __init__(self, settings: Settings, session: AsyncSession) -> None:
        self.settings = settings
        self.session = session

    async def create_access_token(self, user_dto: UserDTO) -> str:
        sid = jwt.encode(
            payload={
                "sub": str(user_dto.id),
                "exp": time.time() + 1000,
                "crt": time.time(),
                # TODO: Add logic for change roles in system.
                "role": json.dumps(Role.EMPLOYEE),
            },
            key=self.settings.certs.private_key,
            algorithm=self.settings.certs.algorithm,
        )
        self.session.add(AuthSession(token=sid, user_id=user_dto.id))
        await self.session.commit()
        return sid
