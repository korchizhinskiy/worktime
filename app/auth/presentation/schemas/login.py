from pydantic import BaseModel
from pydantic.config import ConfigDict


class UserLoginInputSchema(BaseModel):
    username: str
    password: str

    model_config: ConfigDict = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "username": "dev.kor",
                    "password": "123",
                },
            ],
        },
    )
