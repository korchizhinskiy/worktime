from typing import Protocol

type AuthToken = str


class ILogoutRepository(Protocol):
    async def delete_auth_session(
        self,
        token: AuthToken,
    ) -> None: ...
