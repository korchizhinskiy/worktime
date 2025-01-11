from uuid import UUID

from pydantic.config import ConfigDict
from pydantic.main import BaseModel

from app.user.application.enums.roles import Role


class UserDTO(BaseModel):
    id: UUID
    username: str
    password: bytes

    first_name: str
    last_name: str
    second_name: str

    model_config = ConfigDict(from_attributes=True)


class AuthorizedUserDTO(BaseModel):
    id: UUID
    username: str
    password: bytes

    first_name: str
    last_name: str
    second_name: str

    role: Role

    model_config = ConfigDict(from_attributes=True)
