import os

import bcrypt
from fastapi import HTTPException
from core.settings import settings
from app.account.models import User
from app.account.schemas import UserCreatePayload, UserAuthPayload


def make_password(password: str) -> bytes:
    """Get encrypted version of a password"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def check_password(user: User, input_password: str) -> bool:
    """Check user password matches this or not"""
    return bcrypt.checkpw(input_password.encode("utf-8"), hashed_password=user.hashed_password)


async def create_user(dto: UserCreatePayload) -> User:
    """Create new user or raise an error if it's impossible"""
    if await User.filter(email=dto.email).exists():
        raise HTTPException(status_code=400, detail={"email": "Field must be unique"})
    hashed_password: bytes = make_password(password=dto.password)
    return await User.create(**dto.model_dump(), hashed_password=hashed_password)


async def get_user(dto: UserAuthPayload) -> User:
    """Get user by email and password or raise 400 error"""
    user = await User.filter(email=dto.email).first()
    if user is None or not check_password(user, dto.password):
        raise HTTPException(status_code=400, detail="Wrong email or password")
    return user
