from pydantic.main import BaseModel


class UserRegistrationDTO(BaseModel):
    username: str
    password: bytes

    first_name: str
    last_name: str
    second_name: str
