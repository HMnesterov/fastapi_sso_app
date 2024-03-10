from typing import Annotated

from fastapi import APIRouter, Depends
from starlette.responses import RedirectResponse

from app.account.models import User
from app.account.schemas import UserResponse
from app.client.models import Client

from app.oidc import services as oauth_service
from .dependencies import get_or_authorize_user, get_active_token_user
from .schemas import AccessTokenPayload, AccessTokenResponse

router = APIRouter()


@router.get("/oidc/authorize", status_code=200)
async def login_page():  # TODO
    """Return page with auth form / if user is authenticated submit button 'I agreed with app terms' html"""
    return {"ok": True}


@router.post("/oidc/authorize", status_code=303, response_class=RedirectResponse)
async def do_login_oidc(client_id: str,
                        user: User = Depends(get_or_authorize_user)):
    """Authenticate user and redirect him to client domain with generated ?code=..."""
    client: Client = await oauth_service.get_client(client_id)
    # get redirect url
    redirect_url = await oauth_service.get_auth_redirect_url(client=client, user=user)
    return RedirectResponse(url=redirect_url)


@router.post("/oidc/access_token")
async def receive_access_token(access_token_payload: AccessTokenPayload) -> AccessTokenResponse:
    """Generate access token using client data and auth code """
    return await oauth_service.create_access_token(dto=access_token_payload)


@router.post("/oidc/refresh_token")
async def update_access_token():
    """Update access token using given refresh token"""
    raise NotImplementedError()


@router.get("/oidc/userinfo", response_model=UserResponse)
async def get_user_info(user: Annotated[User, Depends(get_active_token_user)]) -> UserResponse:
    """Get oidc user info by scope"""  # TODO add partial data response by scope
    return user
