from pydantic.fields import Field
from pydantic.main import BaseModel

from app.auth.application.dto.profile import (
    AdministratorProfileDTO,
    AssistantManagerProfileDTO,
    ManagerProfileDTO,
    WorkProfileDTO,
)


class UserRegistrationDTO(BaseModel):
    username: str
    password: str

    first_name: str
    last_name: str
    second_name: str
    profile: WorkProfileDTO | ManagerProfileDTO | AssistantManagerProfileDTO | AdministratorProfileDTO = Field(
        ...,
        discriminator="role",
    )


class UserRegistrationHashedDTO(BaseModel):
    username: str
    password: bytes

    first_name: str
    last_name: str
    second_name: str
    profile: WorkProfileDTO | ManagerProfileDTO | AssistantManagerProfileDTO | AdministratorProfileDTO = Field(
        ...,
        discriminator="role",
    )
