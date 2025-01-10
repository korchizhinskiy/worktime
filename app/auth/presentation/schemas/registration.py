from pydantic.config import ConfigDict
from pydantic.main import BaseModel


class UserRegistrationInputSchema(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    second_name: str

    model_config: ConfigDict = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "username": "dev.kor",
                    "password": "123",
                    "first_name": "Nazar",
                    "last_name": "Korchizhinskiy",
                    "second_name": "Alexandrovich",
                },
            ],
        },
    )


class UserRegistrationOutputSchema(BaseModel):
    first_name: str
    last_name: str
    second_name: str
