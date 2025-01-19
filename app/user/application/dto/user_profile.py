from uuid import UUID

from pydantic.config import ConfigDict
from pydantic.main import BaseModel

from app.user.application.enums.roles import Role


class UserDTO(BaseModel):
    id: UUID
    username: str

    first_name: str
    last_name: str
    second_name: str | None

    model_config = ConfigDict(from_attributes=True)


class UserProfileDTO(BaseModel):
    id: UUID
    username: str

    first_name: str
    last_name: str
    second_name: str | None
    role: Role

    model_config = ConfigDict(from_attributes=True)
