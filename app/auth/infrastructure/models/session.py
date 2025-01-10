from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql.schema import ForeignKey
from uuid6 import uuid7

from app.infrastructure.database import Base


if TYPE_CHECKING:
    from app.user.infrastructure.models.user import User


class AuthSession(Base):
    __tablename__: str = "auth__auth_session"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid7)
    token: Mapped[str] = mapped_column()

    user: Mapped["User"] = relationship(cascade="all, delete", back_populates="auth_sessions")
    user_id: Mapped[UUID] = mapped_column(ForeignKey("user__user.id", ondelete="CASCADE"))
