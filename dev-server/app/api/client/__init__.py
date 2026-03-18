from fastapi import APIRouter
from .home import router as home_router

router = APIRouter(prefix="/client")
router.include_router(home_router)
