from fastapi.routing import APIRouter
from .calendar import router as calendar_router

router = APIRouter()

router.include_router(calendar_router)
