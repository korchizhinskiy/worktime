from pydantic.main import BaseModel


class UserRegistrationInputSchema(BaseModel):
    username: str
    password: bytes
    first_name: str
    last_name: str
    second_name: str


class UserRegistrationOutputSchema(BaseModel):
    first_name: str
    last_name: str
    second_name: str
