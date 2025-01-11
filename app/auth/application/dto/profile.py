from pydantic.main import BaseModel

from app.user.application.enums.roles import Role
from app.user.application.enums.specialization import Specialization


class WorkProfile(BaseModel):
    specialization: Specialization


class ManagerProfile(BaseModel):
    pass


class AssistantManagerProfile(BaseModel):
    pass


class AdministratorProfile(BaseModel):
    pass


class Profile(BaseModel):
    role: Role
    info: WorkProfile | ManagerProfile | AssistantManagerProfile | AdministratorProfile
