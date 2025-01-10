from pydantic import BaseModel


class UserLoginInputSchema(BaseModel):
    username: str
    password: bytes
