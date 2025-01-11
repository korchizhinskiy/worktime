from pydantic.main import BaseModel


class UserRegistrationDTO(BaseModel):
    username: str
    password: str

    first_name: str
    last_name: str
    second_name: str
