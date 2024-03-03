from fastapi import HTTPException
from starlette.requests import Request

from .models import User, Session
from ..utils import now


async def get_user_session(request: Request) -> User:
    """Get user by his session or raise exception"""
    session_key = request.cookies.get("session_key")
    if session_key is None:
        raise HTTPException(status_code=401)
    session = await Session.filter(session_key=session_key).select_related("user").first()
    if session is None or session.expire_at < now():
        if session:
            await session.delete()
        raise HTTPException(status_code=401)
    return await session.user
