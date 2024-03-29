from datetime import timedelta

from fastapi import Response

from app.utils import now, generate_random_string
from core.settings import settings
from .models import User, Session


async def add_session(response: Response, user: User) -> None:
    """When log_in"""
    session_key = await generate_session_key()
    session = await Session.create(session_key=session_key,
                                   expire_at=now() + timedelta(days=settings.SESSION_LIFE),
                                   user=user)
    response.set_cookie(key=settings.SESSION_COOKIE_NAME, value=session.session_key)


async def generate_session_key() -> str:
    """Generate unique session key"""
    key = generate_random_string(32)
    while await Session.exists(session_key=key):
        key = generate_random_string(32)
    return key
