from logging import getLogger
from typing import final

import bcrypt

from app.auth.application.dto.login import UserLoginDTO
from app.auth.application.dto.user_token import TokenDTO
from app.auth.application.exceptions.user import UserNotFoundError, WrongPasswordError
from app.auth.application.interfaces.repository.user import IUserRepository
from app.auth.application.services.authentication import JWTService

log = getLogger(__name__)


@final
class UserLoginInteractor:
    def __init__(self, repository: IUserRepository, auth_service: JWTService) -> None:
        self.repository = repository
        self.auth_service = auth_service

    async def execute(self, user_dto: UserLoginDTO) -> TokenDTO:
        user = await self.repository.get_user(user_dto.username)

        if not user:
            raise UserNotFoundError(username=user_dto.username)

        if not bcrypt.checkpw(user_dto.password, user.password):
            raise WrongPasswordError

        token = await self.auth_service.create_access_token(user)
        return TokenDTO(token=token)
