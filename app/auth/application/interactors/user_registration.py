from typing import final

from app.auth.application.dto.registration import UserRegistrationDTO, UserRegistrationHashedDTO
from app.auth.application.exceptions.user import UserAlreadyRegisteredError
from app.auth.application.interfaces.repository.registration import IRegistrationRepository
from app.auth.application.services.security import hash_password


@final
class UserRegistrationInteractor:
    def __init__(self, repository: IRegistrationRepository) -> None:
        self.repository = repository

    async def execute(self, user_dto: UserRegistrationDTO) -> None:
        registered_user = await self.repository.get_user(user_dto.username)

        if registered_user:
            raise UserAlreadyRegisteredError(username=user_dto.username)

        hashed_password = hash_password(bytes(user_dto.password, encoding="utf-8"))

        await self.repository.create(
            UserRegistrationHashedDTO(
                username=user_dto.username,
                first_name=user_dto.first_name,
                last_name=user_dto.last_name,
                second_name=user_dto.second_name,
                password=hashed_password,
            ),
        )
