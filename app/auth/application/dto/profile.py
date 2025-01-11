from typing import Literal
from pydantic.main import BaseModel

from app.user.application.enums.roles import Role
from app.user.application.enums.specialization import Specialization


class WorkProfileDTO(BaseModel):
    role: Literal[Role.EMPLOYEE]
    specialization: Specialization


class ManagerProfileDTO(BaseModel):
    role: Literal[Role.MANAGER]


class AssistantManagerProfileDTO(BaseModel):
    role: Literal[Role.ASSISTANT_MANAGER]


class AdministratorProfileDTO(BaseModel):
    role: Literal[Role.ADMINISTRATOR]
