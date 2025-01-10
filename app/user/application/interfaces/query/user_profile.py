from typing import Protocol

from app.auth.application.dto.user import UserDTO
from app.user.application.dto.user_profile import UserProfileDTO


class IUserProfileQuery(Protocol):
    def execute(self, idp: UserDTO) -> UserProfileDTO: ...
