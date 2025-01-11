from logging import getLogger
from typing import final

import bcrypt

from app.auth.application.dto.login import UserLoginDTO
from app.auth.application.dto.user import AuthorizedUserDTO
from app.auth.application.dto.user_token import TokenDTO
from app.auth.application.exceptions.user import UserNotFoundError, WrongPasswordError
from app.auth.application.interfaces.repository.login import ILoginRepository
from app.auth.application.services.authentication import JWTService

log = getLogger(__name__)


@final
class UserLoginInteractor:
    def __init__(self, repository: ILoginRepository, auth_service: JWTService) -> None:
        self.repository = repository
        self.auth_service = auth_service

    async def execute(self, user_dto: UserLoginDTO) -> TokenDTO:
        user = await self.repository.get_user(user_dto.username)

        if not user:
            raise UserNotFoundError(username=user_dto.username)

        if not bcrypt.checkpw(bytes(user_dto.password, encoding="utf8"), user.password):
            raise WrongPasswordError

        # TODO: Set explicitly field in DTO initialization.
        authorized_user = AuthorizedUserDTO(**user.model_dump(), role=user_dto.role)
        token = await self.auth_service.create_access_token(authorized_user)
        return TokenDTO(token=token)
