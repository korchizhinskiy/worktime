from uuid import UUID

from pydantic.config import ConfigDict
from pydantic.main import BaseModel

from app.user.application.enums.roles import Role


class AuthorizedUserDTO(BaseModel):
    id: UUID
    username: str

    first_name: str
    last_name: str
    second_name: str | None
    role: Role
    token: str

    model_config = ConfigDict(from_attributes=True)
