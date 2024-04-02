from fastapi import APIRouter, Depends
from dependencies.auth import get_current_user

from dependencies.roles import admin_role, moderator_role, user_role
from model import User
from schemas import UserRead

router = APIRouter(prefix="/api/test")

@router.get("/admin")
def admin(curent_user = Depends(admin_role)):
    return "admin content"

@router.get("/user")
def user(current_user = Depends(user_role)):
    return "user content"

@router.get("/mod")
def moderator(current_user = Depends(moderator_role)):
    return "moderator content"

@router.get("/all")
def all():
    return "public content"

@router.get("/profile", response_model=UserRead)
def read_user_me(current_user: User = Depends(get_current_user)):
    user = UserRead(username=current_user.username, email=current_user.email)
    return user