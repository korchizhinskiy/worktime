from typing import Literal

import pytest
import starlette.status as status_code
from httpx import AsyncClient


@pytest.mark.xfail(reason="Not created profile and return password in response.")
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


@pytest.mark.xfail(reason="Return password in response.")
@pytest.mark.asyncio(loop_scope="session")
async def test_registration_user_with_employee_profile(client: AsyncClient) -> None:
    response = await client.post(
        "auth/registration",
        json={
            "username": "petr2024",
            "password": "%PetrSun2024*",
            "first_name": "Petr",
            "last_name": "Sun",
            "second_name": "Alexandrovich",
            "profile": {"role": "EMPLOYEE", "specialization": "BACKEND"},
        },
    )
    assert response.status_code == status_code.HTTP_200_OK
    assert response.json() == {
        "username": "petr2024",
        "first_name": "Petr",
        "last_name": "Sun",
        "second_name": "Alexandrovich",
        "profile": {"role": "EMPLOYEE", "specialization": "BACKEND"},
    }


@pytest.mark.xfail(reason="Return password in response.")
@pytest.mark.asyncio(loop_scope="session")
async def test_registration_user_with_manager_profile(client: AsyncClient) -> None:
    response = await client.post(
        "auth/registration",
        json={
            "username": "petr2024",
            "password": "%PetrSun2024*",
            "first_name": "Petr",
            "last_name": "Sun",
            "second_name": "Alexandrovich",
            "profile": {"role": "MANAGER"},
        },
    )
    assert response.status_code == status_code.HTTP_200_OK
    assert response.json() == {
        "username": "petr2024",
        "first_name": "Petr",
        "last_name": "Sun",
        "second_name": "Alexandrovich",
        "profile": {"role": "MANAGER"},
    }


@pytest.mark.xfail(reason="Return password in response.")
@pytest.mark.asyncio(loop_scope="session")
async def test_registration_user_with_assistant_manager_profile(client: AsyncClient) -> None:
    response = await client.post(
        "auth/registration",
        json={
            "username": "petr2024",
            "password": "%PetrSun2024*",
            "first_name": "Petr",
            "last_name": "Sun",
            "second_name": "Alexandrovich",
            "profile": {"role": "ASSISTANT_MANAGER"},
        },
    )
    assert response.status_code == status_code.HTTP_200_OK
    assert response.json() == {
        "username": "petr2024",
        "first_name": "Petr",
        "last_name": "Sun",
        "second_name": "Alexandrovich",
        "profile": {"role": "ASSISTANT_MANAGER"},
    }


@pytest.mark.xfail(reason="Return password in response.")
@pytest.mark.asyncio(loop_scope="session")
async def test_registration_user_with_administrator_profile(client: AsyncClient) -> None:
    response = await client.post(
        "auth/registration",
        json={
            "username": "petr2024",
            "password": "%PetrSun2024*",
            "first_name": "Petr",
            "last_name": "Sun",
            "second_name": "Alexandrovich",
            "profile": {"role": "ADMINISTRATOR"},
        },
    )
    assert response.status_code == status_code.HTTP_200_OK
    assert response.json() == {
        "username": "petr2024",
        "first_name": "Petr",
        "last_name": "Sun",
        "second_name": "Alexandrovich",
        "profile": {"role": "ADMINISTRATOR"},
    }


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
