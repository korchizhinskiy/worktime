from pydantic.main import BaseModel

from app.user.application.enums.roles import Role


class UserLoginDTO(BaseModel):
    username: str
    password: str
    role: Role
