from dishka.dependency_source.make_factory import provide  # type: ignore [reportUnknownVariableType]
from dishka.entities.scope import Scope
from dishka.provider import Provider

from app.training.application.interface.repository.exercise import IExerciseRepository
from app.training.infrastructure.repository.exercise import ExerciseRepository


class RepositoryProvider(Provider):
    exercise = provide(
        ExerciseRepository,
        provides=IExerciseRepository,
        scope=Scope.REQUEST,
    )
