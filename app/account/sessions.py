import os
from datetime import timedelta

from fastapi import Response

from core.settings import settings
from .models import User, Session
from ..utils import now


async def add_session(response: Response, user: User):
    """When log_in"""
    session_key = await generate_session_key()
    session = await Session.create(session_key=session_key,
                                   expire_at=now() + timedelta(days=settings.SESSION_LIFE),
                                   user=user)
    response.set_cookie(key="session_key", value=session.session_key)


async def generate_session_key() -> str:
    """Generate unique session key"""
    key = os.urandom(32).hex()
    while await Session.exists(session_key=key):
        key = os.urandom(32).hex()
    return key
