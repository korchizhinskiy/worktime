from uuid import UUID

from pydantic.config import ConfigDict
from pydantic.main import BaseModel


class UserProfileDTO(BaseModel):
    id: UUID
    username: str
    password: bytes

    first_name: str
    last_name: str
    second_name: str

    model_config = ConfigDict(from_attributes=True)
