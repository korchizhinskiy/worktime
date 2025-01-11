from typing import Annotated
from dishka.integrations.fastapi import FromDishka, inject
from fastapi.param_functions import Body
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
    user_data: Annotated[
        UserRegistrationInputSchema,
        Body(
            openapi_examples={
                "employee": {
                    "summary": "Employee profile",
                    "description": 'Create user with "Employee" role (profile)',
                    "value": {
                        "username": "dev.kor",
                        "password": "employee_kor",
                        "first_name": "Nazar",
                        "last_name": "Korchizhinskiy",
                        "second_name": "Alexandrovich",
                        "profile": {"role": "EMPLOYEE", "specialization": "BACKEND"},
                    },
                },
                "manager": {
                    "summary": "Manager profile",
                    "description": 'Create user with "Manager" role (profile)',
                    "value": {
                        "username": "dev.kor",
                        "password": "manager_kor",
                        "first_name": "Nazar",
                        "last_name": "Korchizhinskiy",
                        "second_name": "Alexandrovich",
                        "profile": {"role": "MANAGER"},
                    },
                },
                "assistant_manager": {
                    "summary": "Assistant Manager profile",
                    "description": 'Create user with "Assistant Manager" role (profile)',
                    "value": {
                        "username": "dev.kor",
                        "password": "assistant_manager_kor",
                        "first_name": "Nazar",
                        "last_name": "Korchizhinskiy",
                        "second_name": "Alexandrovich",
                        "profile": {"role": "ASSISTANT_MANAGER"},
                    },
                },
                "administrator": {
                    "summary": "Administrator profile",
                    "description": 'Create user with "Administrator" role (profile)',
                    "value": {
                        "username": "dev.kor",
                        "password": "administrator_kor",
                        "first_name": "Nazar",
                        "last_name": "Korchizhinskiy",
                        "second_name": "Alexandrovich",
                        "profile": {"role": "ADMINISTRATOR"},
                    },
                },
            },
        ),
    ],
    interactor: FromDishka[UserRegistrationUseCase],
) -> UserRegistrationInputSchema:
    await interactor.execute(
        UserRegistrationDTO(
            username=user_data.username,
            password=user_data.password,
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            second_name=user_data.second_name,
            profile=user_data.profile.model_dump(),
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
