from typing import Annotated
from uuid import UUID

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

auth_scheme = HTTPBearer()

# TODO: Check for returning this DTO in Depends functions.
class AuthUserDTO(BaseModel):
    id: UUID
    username: str

    first_name: str
    last_name: str
    second_name: str

    model_config = ConfigDict(from_attributes=True)


@inject
async def get_authenticated_user(
    token: Annotated[HTTPAuthorizationCredentials, Depends(auth_scheme)],
    session: FromDishka[AsyncSession],
) -> AuthUserDTO:
    query = select(AuthSession).options(joinedload(AuthSession.user)).where(AuthSession.token == token.credentials)
    auth_session = await session.scalar(query)

    if not auth_session:
        raise InvalidAuthenticationTokenError
    return AuthUserDTO.model_validate(auth_session.user)
