from dishka.dependency_source.make_factory import provide  # type: ignore [reportUnknownVariableType]
from dishka.entities.scope import Scope
from dishka.provider import Provider

from app.user.application.interfaces.query.user_profile import IUserProfileQuery
from app.user.infrastructure.query.user_profile import UserProfileQuery


class QueryProvider(Provider):
    user_profile_query = provide(
        UserProfileQuery,
        provides=IUserProfileQuery,
        scope=Scope.REQUEST,
    )
