from fastapi import APIRouter, Depends

import app.oauth2.services as oauth_service
from .schemas import ClientPayload, ClientCreateResponse, ClientResponse
from ..account.dependencies import get_user_session
from ..account.models import User

app = APIRouter()


@app.post("/clients", response_model=ClientCreateResponse)
async def create_oauth_client(client_payload: ClientPayload, user: User = Depends(get_user_session)):
    """Create new client to manage auth flow"""
    return await oauth_service.register_client(user, dto=client_payload)


@app.put("/clients/{client_id}", response_model=ClientResponse)
async def update_oauth_client(client_id: str,
                              client_payload: ClientPayload,
                              user: User = Depends(get_user_session)):
    """Update client auth flow settings"""
    client = await oauth_service.get_client(client_id, user)
    return await oauth_service.update_client(client=client, dto=client_payload)

