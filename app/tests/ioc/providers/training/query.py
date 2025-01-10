from dishka.dependency_source.make_factory import provide  # type: ignore [reportUnknownVariableType]
from dishka.entities.scope import Scope
from dishka.provider import Provider

from app.training.application.interface.query.exercise import IExerciseListQuery, IExerciseQuery
from app.training.application.interface.query.exercise_group import IExerciseGroupListQuery, IExerciseGroupQuery
from app.training.infrastructure.query.exercise import ExerciseListQuery, ExerciseQuery
from app.training.infrastructure.query.exercise_group import ExerciseGroupListQuery, ExerciseGroupQuery


class QueryProvider(Provider):
    exercise_query = provide(
        ExerciseQuery,
        provides=IExerciseQuery,
        scope=Scope.REQUEST,
    )
    exercise_list_query = provide(
        ExerciseListQuery,
        provides=IExerciseListQuery,
        scope=Scope.REQUEST,
    )
    exercise_group_query = provide(
        ExerciseGroupQuery,
        provides=IExerciseGroupQuery,
        scope=Scope.REQUEST,
    )
    exercise_group_list_query = provide(
        ExerciseGroupListQuery,
        provides=IExerciseGroupListQuery,
        scope=Scope.REQUEST,
    )
