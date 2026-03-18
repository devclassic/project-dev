from fastapi import APIRouter
from .admin import router as admin_router
from .client import router as client_router
from ..utils.data import db


router = APIRouter(prefix="/api")
router.include_router(admin_router)
router.include_router(client_router)


@router.get("/init")
def init():
    user = db["users"].find_one(dict(username="admin"))
    if user:
        return {"message": "无需初始化"}
    db["users"].insert(dict(username="admin", password="123456", token=""))
    return {"message": "初始化成功"}
