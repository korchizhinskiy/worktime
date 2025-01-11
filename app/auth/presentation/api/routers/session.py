from typing import Annotated
from dishka.integrations.fastapi import FromDishka, inject
from fastapi.param_functions import Depends
from fastapi.routing import APIRouter

from app.auth.application.dto.user import UserDTO
from app.auth.application.interfaces.usecase.change_role import UserChangeRoleUseCase
from app.auth.infrastructure.dependencies import get_authenticated_user
from app.user.application.enums.roles import Role


router = APIRouter(tags=["Session"], prefix="/auth/session")


@router.post("/change-role")
@inject
async def change_user_session_role(
    role: Role,
    interactor: FromDishka[UserChangeRoleUseCase],
    idp: Annotated[UserDTO, Depends(get_authenticated_user)],
) -> None | str:
    return await interactor.execute(role, idp)
