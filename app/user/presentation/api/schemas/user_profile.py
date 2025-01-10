from uuid import UUID

from pydantic import BaseModel


class UserProfileOutputSchema(BaseModel):
    id: UUID
    username: str

    first_name: str
    last_name: str
    second_name: str
