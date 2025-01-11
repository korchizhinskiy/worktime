from pydantic import Field
from pydantic.main import BaseModel

from app.auth.presentation.schemas.profile import (
    AdministratorProfileInputSchema,
    AssistantManagerProfileInputSchema,
    ManagerProfileInputSchema,
    WorkProfileInputSchema,
)


class UserRegistrationInputSchema(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    second_name: str
    profile: (
        WorkProfileInputSchema
        | ManagerProfileInputSchema
        | AssistantManagerProfileInputSchema
        | AdministratorProfileInputSchema
    ) = Field(..., discriminator="role")


class UserRegistrationOutputSchema(BaseModel):
    first_name: str
    last_name: str
    second_name: str
