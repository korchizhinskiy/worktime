from typing import TYPE_CHECKING, final
from uuid import UUID

from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy.orm.base import Mapped
from sqlalchemy.orm.properties import ForeignKey
from uuid6 import uuid7

from app.infrastructure.database import Base

if TYPE_CHECKING:
    from app.user.infrastructure.models.user import User


@final
class AssistantManagerProfile(Base):
    __tablename__: str = "user__assistant_manager_profile"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid7)

    user: Mapped["User"] = relationship(
        cascade="all, delete",
        back_populates="assistant_manager_profile",
        single_parent=True,
    )
    user_id: Mapped[UUID] = mapped_column(ForeignKey("user__user.id", ondelete="CASCADE"))
