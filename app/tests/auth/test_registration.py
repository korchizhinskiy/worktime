from typing import Literal

import pytest
import starlette.status as status_code
from httpx import AsyncClient
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.sql.expression import insert

from app.auth.application.services.security import hash_password
from app.auth.infrastructure.models.user import User


@pytest.mark.xfail(reason="Return password in response.")
@pytest.mark.asyncio(loop_scope="session")
async def test_registration_user(client: AsyncClient) -> None:
    response = await client.post(
        "auth/registration",
        json={
            "username": "petr2024",
            "password": "%PetrSun2024*",
            "first_name": "Petr",
            "last_name": "Sun",
            "second_name": "Alexandrovich",
        },
    )
    assert response.status_code == status_code.HTTP_200_OK
    assert response.json() == {
        "username": "petr2024",
        "first_name": "Petr",
        "last_name": "Sun",
        "second_name": "Alexandrovich",
    }


@pytest.mark.asyncio(loop_scope="session")
async def test_repeatable_user_registration(client: AsyncClient, session: AsyncSession) -> None:
    # Arrange
    stmt = insert(User).values(
        username="petr2024",
        password=hash_password(b"%PetrSun2024*"),
        first_name="Petr",
        last_name="Sun",
        second_name="Alexandrovich",
    )
    await session.execute(stmt)

    # Act
    response = await client.post(
        "auth/registration",
        json={
            "username": "petr2024",
            "password": "%PetrSun2024*",
            "first_name": "Petr",
            "last_name": "Sun",
            "second_name": "Alexandrovich",
        },
    )
    assert response.status_code == status_code.HTTP_400_BAD_REQUEST


@pytest.mark.parametrize(
    ("excluded_variable", "status_code"),
    (
        ("username", status_code.HTTP_422_UNPROCESSABLE_ENTITY),
        ("password", status_code.HTTP_422_UNPROCESSABLE_ENTITY),
        ("first_name", status_code.HTTP_422_UNPROCESSABLE_ENTITY),
        ("last_name", status_code.HTTP_422_UNPROCESSABLE_ENTITY),
        pytest.param(
            "second_name",
            status_code.HTTP_200_OK,
            marks=pytest.mark.xfail(reason="Second name must be not required."),
        ),
    ),
)
@pytest.mark.asyncio(loop_scope="session")
async def test_registration_without_any_parameter(
    client: AsyncClient,
    excluded_variable: str,
    status_code: Literal[422, 200],
) -> None:
    json = {
        "username": "petr2024",
        "password": "%PetrSun2024*",
        "first_name": "Petr",
        "last_name": "Sun",
        "second_name": "Alexandrovich",
    }
    json.pop(excluded_variable)
    response = await client.post(
        "auth/registration",
        json=json,
    )
    assert response.status_code == status_code
