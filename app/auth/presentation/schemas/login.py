from pydantic import BaseModel
from pydantic.config import ConfigDict

from app.user.application.enums.roles import Role


class UserLoginInputSchema(BaseModel):
    username: str
    password: str
    role: Role

    model_config: ConfigDict = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "username": "dev.kor",
                    "password": "123",
                    "role": "EMPLOYEE",
                },
            ],
        },
    )
