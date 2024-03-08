from fastapi import APIRouter, Depends

import app.client.services as oauth_service
from .schemas import ClientPayload, ClientCreateResponse, ClientResponse
from ..account.dependencies import get_current_user
from ..account.models import User

app = APIRouter()


@app.post("/clients", response_model=ClientCreateResponse)
async def create_client(client_payload: ClientPayload, user: User = Depends(get_current_user)):
    """Create new client to manage auth flow"""
    return await oauth_service.register_client(user, dto=client_payload)


@app.put("/clients/{client_id}", response_model=ClientResponse)
async def update_client(client_id: str,
                        client_payload: ClientPayload,
                        user: User = Depends(get_current_user)):
    """Update client auth flow settings"""
    client = await oauth_service.get_client(client_id, user)
    return await oauth_service.update_client(client=client, dto=client_payload)


@app.get("/clients/{client_id}", response_model=ClientResponse)
async def get_client(client_id: str,
                     user: User = Depends(get_current_user)):
    """Return client data"""
    return await oauth_service.get_client(client_id, user)
