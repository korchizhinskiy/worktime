from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from functools import partial

from fastapi import FastAPI, Response, status
from fastapi.requests import Request
from fastapi.responses import ORJSONResponse

from app.auth.application.exceptions.base import ApplicationError
from app.auth.application.exceptions.user import UserAlreadyRegisteredError, UserNotFoundError, WrongPasswordError
from app.auth.infrastructure.exceptions import InvalidAuthenticationTokenError


@dataclass(frozen=True)
class ErrorData:
    message: str = "Unknown error occurred"


@dataclass(frozen=True)
class ErrorResponse:
    error: ErrorData


def setup_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(UserNotFoundError, error_handler(status.HTTP_404_NOT_FOUND))
    app.add_exception_handler(UserAlreadyRegisteredError, error_handler(status.HTTP_400_BAD_REQUEST))
    app.add_exception_handler(WrongPasswordError, error_handler(status.HTTP_400_BAD_REQUEST))
    app.add_exception_handler(InvalidAuthenticationTokenError, error_handler(status.HTTP_401_UNAUTHORIZED))

    app.add_exception_handler(ApplicationError, error_handler(status.HTTP_500_INTERNAL_SERVER_ERROR))
    app.add_exception_handler(Exception, unknown_exception_handler)


def error_handler(status_code: int) -> Callable[..., Awaitable[Response]]:
    return partial(app_error_handler, status_code=status_code)


async def app_error_handler(request_: Request, exc: ApplicationError, status_code: int) -> Response:  # noqa: ARG001
    return await handle_error(
        err_data=ErrorData(message=exc.message),
        status_code=status_code,
    )


async def unknown_exception_handler(request_: Request, exc_: Exception) -> Response:  # noqa: ARG001
    # TODO: Add sentry logs in to this function.
    return await handle_error(err_data=ErrorData(message="Unknown error occurred"), status_code=500)


async def handle_error(  # noqa: RUF029
    err_data: ErrorData,
    status_code: int,
) -> Response:
    return ORJSONResponse(
        content=ErrorResponse(error=err_data),
        status_code=status_code,
    )
