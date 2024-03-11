from datetime import timedelta

from fastapi import HTTPException
from starlette import status
from core.settings import settings
from app.utils import now

from app.account import services as acc_service
from app.account.models import User
from app.client.models import Client
from app.client import services as client_service

from .jwt import create_jwt_token, decode_jwt_token
from .schemas import AccessTokenPayload, AccessTokenResponse, AuthTokenScheme, AccessTokenScheme


async def get_auth_redirect_url(client: Client, user: User) -> str:
    """Get client redirect url for authenticated user"""
    token = generate_auth_token(client, user)
    link = f"{client.callback_url}?code={token}"
    return link


def generate_auth_token(client: Client, user: User) -> str:
    """Get temporary jwt token which is used to receive access token"""
    token_data: AuthTokenScheme = AuthTokenScheme(user_id=user.id,
                                                  client_id=client.client_id,
                                                  expire_at=now() + timedelta(minutes=5))
    return create_jwt_token(token_data=token_data)  # 5 minutes


async def create_access_token(dto: AccessTokenPayload) -> AccessTokenResponse:
    """Create new jwt access and refresh tokens"""
    client = await client_service.get_client_by_id(dto.client_id)
    if not acc_service.check_encrypted(hashed_password=client.client_secret, input_password=dto.client_secret):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    # decrypt jwt
    token_data: AuthTokenScheme = AuthTokenScheme(**decode_jwt_token(dto.code))
    if dto.client_id != token_data.client_id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    user: User = await acc_service.get_user_by_id(user_id=token_data.user_id)
    # get tokens
    return generate_access_and_refresh_token(access_token_payload=dto, user=user)


def generate_access_and_refresh_token(access_token_payload: AccessTokenPayload, user: User) -> AccessTokenResponse:
    """Generate new access and refresh tokens"""
    # get access token
    token_data = {"user_id": user.id, **access_token_payload.model_dump()}
    access_token_data = AccessTokenScheme(**token_data,
                                          expire_at=now() + timedelta(hours=12))
    refresh_data = AccessTokenScheme(**token_data,
                                     expire_at=now() + timedelta(days=settings.SESSION_LIFE))
    return AccessTokenResponse(
        access_token=create_jwt_token(access_token_data),
        refresh_token=create_jwt_token(refresh_data)
    )
