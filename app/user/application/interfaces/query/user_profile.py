from typing import Protocol

from app.infrastructure.schemas.auth_user import AuthorizedUserDTO
from app.user.application.dto.user_profile import UserProfileDTO


class IUserProfileQuery(Protocol):
    def execute(self, idp: AuthorizedUserDTO) -> UserProfileDTO: ...
