from pydantic.main import BaseModel


class UserLoginDTO(BaseModel):
    username: str
    password: bytes
