from typing import Annotated
from dishka.integrations.fastapi import FromDishka, inject
from fastapi.param_functions import Depends
from fastapi.routing import APIRouter

from app.auth.application.dto.login import UserLoginDTO
from app.auth.application.dto.registration import UserRegistrationDTO
from app.auth.application.dto.user import UserDTO
from app.auth.application.dto.user_token import TokenDTO
from app.auth.application.interfaces.usecase.change_role import UserChangeRoleUseCase
from app.auth.application.interfaces.usecase.user_login import UserLoginUseCase
from app.auth.application.interfaces.usecase.user_registration import UserRegistrationUseCase
from app.auth.infrastructure.dependencies import get_authenticated_user
from app.auth.presentation.schemas.login import UserLoginInputSchema
from app.auth.presentation.schemas.registration import UserRegistrationInputSchema
from app.user.application.enums.roles import Role

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
        UserLoginDTO(username=user_data.username, password=user_data.password, role=user_data.role),
    )


@router.post("/change-role")
@inject
async def change_user_role(
    role: Role,
    interactor: FromDishka[UserChangeRoleUseCase],
    idp: Annotated[UserDTO, Depends(get_authenticated_user)],
) -> None | str:
    return await interactor.execute(role, idp)
