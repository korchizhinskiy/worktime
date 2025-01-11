from typing import Literal
from pydantic.main import BaseModel

from app.user.application.enums.roles import Role
from app.user.application.enums.specialization import Specialization


class WorkProfileInputSchema(BaseModel):
    role: Literal[Role.EMPLOYEE]
    specialization: Specialization


class ManagerProfileInputSchema(BaseModel):
    role: Literal[Role.MANAGER]


class AssistantManagerProfileInputSchema(BaseModel):
    role: Literal[Role.ASSISTANT_MANAGER]


class AdministratorProfileInputSchema(BaseModel):
    role: Literal[Role.ADMINISTRATOR]
