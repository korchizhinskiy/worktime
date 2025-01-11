from fastapi.routing import APIRouter
from .auth import router as auth_router
from .session import router as session_router


router = APIRouter()
router.include_router(auth_router)
router.include_router(session_router)
