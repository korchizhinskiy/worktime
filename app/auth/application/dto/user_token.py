from pydantic.main import BaseModel

type UserToken = str


class TokenDTO(BaseModel):
    token: UserToken
