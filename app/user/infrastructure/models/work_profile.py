from typing import TYPE_CHECKING, final
from uuid import UUID

from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy.orm.base import Mapped
from sqlalchemy.orm.properties import ForeignKey
from sqlalchemy.sql.sqltypes import Enum
from uuid6 import uuid7

from app.infrastructure.database import Base
from app.user.application.enums.specialization import Specialization

if TYPE_CHECKING:
    from app.user.infrastructure.models.user import User


@final
class WorkProfile(Base):
    __tablename__: str = "user__work_profile"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid7)
    specialization: Mapped[Specialization] = mapped_column(Enum(Specialization))

    user: Mapped["User"] = relationship(cascade="all, delete", back_populates="work_profile", single_parent=True)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("user__user.id", ondelete="CASCADE"))
