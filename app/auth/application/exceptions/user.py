from app.auth.application.exceptions.base import ApplicationError


class UserNotFoundError(ApplicationError):
    message: str

    def __init__(self, *, username: str | None = None) -> None:
        if username:
            self.message = f"User with username {username!r} not found in system"
        else:
            self.message = "User not found in system"
        super().__init__()


class UserAlreadyRegisteredError(ApplicationError):
    message: str

    def __init__(self, *, username: str | None = None) -> None:
        if username:
            self.message = f"User with username {username!r} already registered."
        else:
            self.message = "User already registred in system"
        super().__init__()


class WrongPasswordError(ApplicationError):
    message: str = "Wrond password for this user"
