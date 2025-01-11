from typing import Annotated
from uuid import UUID

import jwt
from dishka.integrations.fastapi import FromDishka, inject
from fastapi.param_functions import Depends
from fastapi.security.http import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel
from pydantic.config import ConfigDict
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm.strategy_options import joinedload
from sqlalchemy.sql.expression import select

from app.auth.infrastructure.exceptions import InvalidAuthenticationTokenError
from app.auth.infrastructure.models.session import AuthSession
from app.infrastructure.config import Settings
from app.user.application.enums.roles import Role

auth_scheme = HTTPBearer()


# TODO: Check for returning this DTO in Depends functions.
class AuthUserDTO(BaseModel):
    id: UUID
    username: str

    first_name: str
    last_name: str
    second_name: str | None
    role: Role
    token: str

    model_config = ConfigDict(from_attributes=True)


# TODO: Add current user role into dto (from JWT)
@inject
async def get_authenticated_user(
    token: Annotated[HTTPAuthorizationCredentials, Depends(auth_scheme)],
    session: FromDishka[AsyncSession],
    settings: FromDishka[Settings],
) -> AuthUserDTO:
    query = select(AuthSession).options(joinedload(AuthSession.user)).where(AuthSession.token == token.credentials)
    auth_session = await session.scalar(query)

    if not auth_session:
        raise InvalidAuthenticationTokenError

    user_role = jwt.decode(
        token.credentials,
        key=settings.certs.public_key,
        algorithms=settings.certs.algorithm,
    ).get("role")

    if not user_role:
        # TODO: Set custom infrastructure exception.
        raise Exception("User token must containt role.")

    return AuthUserDTO(
        id=auth_session.user.id,
        username=auth_session.user.username,
        first_name=auth_session.user.first_name,
        last_name=auth_session.user.last_name,
        second_name=auth_session.user.second_name,
        role=Role[user_role],
        token=token.credentials,
    )
