from typing import Protocol


class UnitOfWork(Protocol):
    async def commit(self) -> None:
        pass

    async def rollback(self) -> None:
        pass
