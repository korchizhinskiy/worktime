from dishka.integrations.fastapi import FromDishka, inject
from fastapi.routing import APIRouter

from app.auth.application.dto.login import UserLoginDTO
from app.auth.application.dto.registration import UserRegistrationDTO
from app.auth.application.dto.user_token import TokenDTO
from app.auth.application.interfaces.usecase.user_login import UserLoginUseCase
from app.auth.application.interfaces.usecase.user_registration import UserRegistrationUseCase
from app.auth.presentation.schemas.login import UserLoginInputSchema
from app.auth.presentation.schemas.registration import UserRegistrationInputSchema

router = APIRouter(tags=["Auth"], prefix="/auth")


@router.post("/registration")
@inject
async def registration(
    user_data: UserRegistrationInputSchema,
    interactor: FromDishka[UserRegistrationUseCase],
) -> UserRegistrationInputSchema:
    await interactor.execute(
        UserRegistrationDTO(
            username=user_data.username,
            password=user_data.password,
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            second_name=user_data.second_name,
        ),
    )
    return user_data


@router.post("/login")
@inject
async def login(
    user_data: UserLoginInputSchema,
    interactor: FromDishka[UserLoginUseCase],
) -> TokenDTO:
    return await interactor.execute(
        UserLoginDTO(username=user_data.username, password=user_data.password),
    )
