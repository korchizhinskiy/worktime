from uuid import UUID

from pydantic import BaseModel
from pydantic.config import ConfigDict

from app.auth.application.dto.profile import (
    AdministratorProfileDTO,
    AssistantManagerProfileDTO,
    ManagerProfileDTO,
    WorkProfileDTO,
)


class UserProfileOutputSchema(BaseModel):
    id: UUID
    username: str

    first_name: str
    last_name: str
    second_name: str

    profile: WorkProfileDTO | ManagerProfileDTO | AssistantManagerProfileDTO | AdministratorProfileDTO
    model_config: ConfigDict = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "username": "dev.kor",
                    "first_name": "Nazar",
                    "last_name": "Korchizhinskiy",
                    "second_name": "Alexandrovich",
                },
            ],
        },
    )
