from typing import TYPE_CHECKING, final
from uuid import UUID

from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy.orm.base import Mapped
from uuid6 import uuid7

from app.infrastructure.database import Base


if TYPE_CHECKING:
    from app.auth.infrastructure.models.session import AuthSession


@final
class User(Base):
    __tablename__: str = "user__user"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid7)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[bytes] = mapped_column()

    first_name: Mapped[str] = mapped_column()
    last_name: Mapped[str] = mapped_column()
    second_name: Mapped[str | None] = mapped_column()

    auth_sessions: Mapped[list["AuthSession"]] = relationship(back_populates="user")
