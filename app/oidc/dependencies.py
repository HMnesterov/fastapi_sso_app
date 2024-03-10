from typing import TypeVar

from fastapi import Depends
from starlette.requests import Request
from app.oidc import services as oidc_service
from app.account.models import User
from app.account import services as acc_service
from app.account.schemas import UserAuthPayload
from app.account.dependencies import get_current_user
from app.oidc.jwt import decode_jwt_token, oauth2_scheme
from app.oidc.schemas import TokenUserBaseModel


async def get_or_authorize_user(request: Request, user_payload: UserAuthPayload = None) -> User:
    """Authorize  user using payload if sent else by session key"""
    if user_payload is not None:
        return await acc_service.get_user(user_payload)
    return await get_current_user(request)


async def get_active_token_user(token: str = Depends(oauth2_scheme)) -> User:
    user_data: TokenUserBaseModel = TokenUserBaseModel(**decode_jwt_token(token))
    return await oidc_service.get_user_by_id(user_data.user_id)
