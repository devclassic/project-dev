from fastapi import APIRouter
from .admin import router as admin_router
from .client import router as client_router


router = APIRouter(prefix="/api")
router.include_router(admin_router)
router.include_router(client_router)
