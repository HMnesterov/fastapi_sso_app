from fastapi import HTTPException
from starlette.requests import Request

from .models import User, Session
from app.utils import now


async def update_last_login(user: User) -> User:
    user.last_login = now()
    await user.save()
    return user


async def get_current_user(request: Request) -> User:
    """Get user by his session or raise exception"""
    session_key = request.cookies.get("session_key")
    if session_key is None:
        raise HTTPException(status_code=401)
    session = await Session.filter(session_key=session_key).select_related("user").first()
    if session is None or session.expire_at < now():
        if session:
            await session.delete()
        raise HTTPException(status_code=401)
    return await update_last_login(session.user)
