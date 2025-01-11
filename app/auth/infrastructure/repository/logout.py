from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.sql.expression import delete

from app.auth.application.interfaces.repository.logout import ILogoutRepository
from app.auth.infrastructure.models.session import AuthSession

type AuthToken = str


class LogoutRepository(ILogoutRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def delete_auth_session(self, token: AuthToken) -> None:
        stmt = delete(AuthSession).where(AuthSession.token == token)
        await self.session.execute(stmt)
        await self.session.commit()
