from typing import Annotated

from dishka.integrations.fastapi import FromDishka, inject
from fastapi.param_functions import Depends
from fastapi.routing import APIRouter

from app.auth.application.interfaces.usecase.change_role import UserChangeRoleUseCase
from app.auth.application.interfaces.usecase.logout import UserLogoutUseCase
from app.auth.infrastructure.dependencies import AuthUserDTO, get_authenticated_user
from app.user.application.enums.roles import Role

router = APIRouter(tags=["Session"], prefix="/auth/session")


@router.post("/change-role")
@inject
async def change_user_session_role(
    role: Role,
    interactor: FromDishka[UserChangeRoleUseCase],
    idp: Annotated[AuthUserDTO, Depends(get_authenticated_user)],
) -> None | str:
    return await interactor.execute(role, idp)


@router.post("/logout")
@inject
async def logout_user_session(
    interactor: FromDishka[UserLogoutUseCase],
    idp: Annotated[AuthUserDTO, Depends(get_authenticated_user)],
) -> None | str:
    return await interactor.execute(idp)
