from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio.session import AsyncSession


class SQLAlchemyUoW:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def commit(self) -> None:
        try:
            await self._session.commit()
        except SQLAlchemyError as error:
            raise ValueError("ERROR") from error

    async def rollback(self) -> None:
        try:
            await self._session.rollback()
        except SQLAlchemyError as error:
            raise ValueError("ERROR") from error
