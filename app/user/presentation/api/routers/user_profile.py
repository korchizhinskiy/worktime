from typing import Annotated

from dishka.integrations.fastapi import FromDishka, inject
from fastapi import Depends
from fastapi.routing import APIRouter

from app.auth.application.dto.user import UserDTO
from app.auth.infrastructure.dependencies import get_authenticated_user
from app.user.application.dto.user_profile import UserProfileDTO
from app.user.application.interfaces.query.user_profile import IUserProfileQuery
from app.user.presentation.api.schemas.user_profile import UserProfileOutputSchema

router = APIRouter(tags=["User Profile"], prefix="/user")


@router.get("/profile", response_model=UserProfileOutputSchema)
@inject
# TODO: Change DTO to OutSchema
def get_user_profile(
    query: FromDishka[IUserProfileQuery],
    idp: Annotated[UserDTO, Depends(get_authenticated_user)],
) -> UserProfileDTO:
    return query.execute(idp=idp)
