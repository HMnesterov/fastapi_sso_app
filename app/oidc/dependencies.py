from fastapi import Depends
from starlette.requests import Request

from app.account import services as acc_service
from app.account.dependencies import get_session_user
from app.account.models import User
from app.account.schemas import UserAuthPayload
from .jwt import decode_jwt_token, oauth2_scheme
from .schemas import TokenUserBaseScheme


async def get_or_authorize_user(request: Request, user_payload: UserAuthPayload = None) -> User:
    """Authorize  user using payload if sent else by session key"""
    if user_payload is not None:
        return await acc_service.get_user(user_payload)
    return await get_session_user(request)


async def get_active_token_user(token: str = Depends(oauth2_scheme)) -> User:
    """Get current user by token"""
    user_data: TokenUserBaseScheme = TokenUserBaseScheme(**decode_jwt_token(token))
    return await acc_service.get_user_by_id(user_data.user_id)
