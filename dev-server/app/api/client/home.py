from fastapi import APIRouter
from ...data import db

router = APIRouter(prefix="/home")


@router.get("")
def login():
    db["home"].insert({"name": "woaiwhr001", "password": "123456"})
    return {"message": "home"}
