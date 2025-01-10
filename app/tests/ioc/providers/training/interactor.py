from dishka.dependency_source.make_context_var import from_context
from dishka.dependency_source.make_factory import provide  # type: ignore [reportUnknownVariableType]
from dishka.entities.scope import Scope
from dishka.provider import Provider

from app.training.application.interactor.exercise import ExerciseCreationInteractor
from app.training.application.interface.use_case.exercise import ExerciseCreationUseCase


class InteractorProvider(Provider):
    exercise = provide(
        ExerciseCreationInteractor,
        provides=ExerciseCreationUseCase,
        scope=Scope.REQUEST,
    )
