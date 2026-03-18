from fastapi import APIRouter, Body, Header
from ...utils.data import db
import uuid

router = APIRouter(prefix="/auth")


@router.post("/login")
def login(body: dict = Body()):
    username = body.get("username")
    password = body.get("password")
    if not username or not password:
        return {"success": False, "message": "账号或密码不能为空"}
    user = db["users"].find_one(username=username, password=password)
    if user:
        token = str(uuid.uuid4())
        db["users"].update(dict(id=user["id"], token=token), ["id"])
        return {"success": True, "message": "登录成功", "data": token}
    return {"success": False, "message": "账号或密码错误"}


@router.post("/check")
def check(token: str = Header("")):
    user = db["users"].find_one(token=token)
    if user:
        return {"success": True, "message": "已登录"}
    return {"success": False, "message": "未登录"}
