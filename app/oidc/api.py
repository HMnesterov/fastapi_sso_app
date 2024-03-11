from typing import Annotated

from fastapi import APIRouter, Depends

from app.account.models import User
from app.account.schemas import UserResponse
from app.client.models import Client
from app.client.dependencies import get_valid_client

from . import services as oauth_service
from .dependencies import get_or_authorize_user, get_active_token_user
from .schemas import AccessTokenPayload, AccessTokenResponse

router = APIRouter()


@router.post("/oidc/authorize", status_code=200)
async def do_login_oidc(client: Client = Depends(get_valid_client),
                        user: User = Depends(get_or_authorize_user)) -> str:
    """Authorize user and return redirect url for frontend"""
    # get redirect url
    redirect_url = await oauth_service.get_auth_redirect_url(client=client, user=user)
    return redirect_url


@router.post("/oidc/access_token", status_code=200, response_model=AccessTokenResponse)
async def receive_access_token(access_token_payload: AccessTokenPayload) -> AccessTokenResponse:
    """Generate access token using client data and auth code """
    return await oauth_service.create_access_token(dto=access_token_payload)


@router.post("/oidc/refresh_token")
async def update_access_token():
    """Update access token using given refresh token"""
    raise NotImplementedError()


@router.get("/oidc/userinfo", status_code=200, response_model=UserResponse)
async def get_user_info(user: Annotated[User, Depends(get_active_token_user)]) -> UserResponse:
    """Get oidc user info by scope"""  # TODO add partial data response by scope
    return user
