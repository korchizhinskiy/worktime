import pytest
import starlette.status as status_code
from httpx import AsyncClient
from sqlalchemy.ext.asyncio.session import AsyncSession

from app.auth.application.services.security import hash_password
from app.user.application.enums.specialization import Specialization
from app.user.infrastructure.models.administrator_profile import AdministratorProfile
from app.user.infrastructure.models.assistant_manager_profile import AssistantManagerProfile
from app.user.infrastructure.models.manager_profile import ManagerProfile
from app.user.infrastructure.models.user import User
from app.user.infrastructure.models.work_profile import WorkProfile


@pytest.mark.asyncio(loop_scope="session")
async def test_repeatable_user_registration_with_employee_profile(client: AsyncClient, session: AsyncSession) -> None:
    # Arrange
    user = User(
        username="petr2024",
        password=hash_password(b"%PetrSun2024*"),
        first_name="Petr",
        last_name="Sun",
        second_name="Alexandrovich",
    )
    profile = WorkProfile(user=user, specialization=Specialization.BACKEND)
    session.add(user)
    session.add(profile)
    await session.commit()

    # Act
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

    assert response.status_code == status_code.HTTP_400_BAD_REQUEST


@pytest.mark.asyncio(loop_scope="session")
async def test_repeatable_user_registration_with_manager_profile(client: AsyncClient, session: AsyncSession) -> None:
    # Arrange
    user = User(
        username="petr2024",
        password=hash_password(b"%PetrSun2024*"),
        first_name="Petr",
        last_name="Sun",
        second_name="Alexandrovich",
    )
    profile = ManagerProfile(user=user)
    session.add(user)
    session.add(profile)
    await session.commit()

    # Act
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

    assert response.status_code == status_code.HTTP_400_BAD_REQUEST


@pytest.mark.asyncio(loop_scope="session")
async def test_repeatable_user_registration_with_assistant_manager_profile(
    client: AsyncClient,
    session: AsyncSession,
) -> None:
    # Arrange
    user = User(
        username="petr2024",
        password=hash_password(b"%PetrSun2024*"),
        first_name="Petr",
        last_name="Sun",
        second_name="Alexandrovich",
    )
    profile = AssistantManagerProfile(user=user)
    session.add(user)
    session.add(profile)
    await session.commit()

    # Act
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

    assert response.status_code == status_code.HTTP_400_BAD_REQUEST


@pytest.mark.asyncio(loop_scope="session")
async def test_repeatable_user_registration_with_administrator_profile(
    client: AsyncClient,
    session: AsyncSession,
) -> None:
    # Arrange
    user = User(
        username="petr2024",
        password=hash_password(b"%PetrSun2024*"),
        first_name="Petr",
        last_name="Sun",
        second_name="Alexandrovich",
    )
    profile = AdministratorProfile(user=user)
    session.add(user)
    session.add(profile)
    await session.commit()

    # Act
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

    assert response.status_code == status_code.HTTP_400_BAD_REQUEST
