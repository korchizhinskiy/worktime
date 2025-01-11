from fastapi.routing import APIRouter

router = APIRouter(tags=["Worktime"])


@router.get("calendar/")
def get_calendar() -> dict:
    return {}
