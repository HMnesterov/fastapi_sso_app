from fastapi import APIRouter, Depends
from app.account.dependencies import get_session_user
from app.account.models import User
from . import services as client_service
from .dependencies import get_available_client
from .models import Client
from .schemas import ClientPayload, ClientCreateResponse, ClientResponse

router = APIRouter()


@router.post("/clients", response_model=ClientCreateResponse, status_code=201)
async def create_client(client_payload: ClientPayload, user: User = Depends(get_session_user)):
    """Create new client to manage auth flow"""
    return await client_service.register_client(user, dto=client_payload)


@router.put("/clients/{client_id}", response_model=ClientResponse, status_code=200)
async def update_client(
        client_payload: ClientPayload,
        client: Client = Depends(get_available_client)):
    """Update client auth flow settings"""
    return await client_service.update_client(client=client, dto=client_payload)


@router.get("/clients/{client_id}", response_model=ClientResponse, status_code=200)
async def get_client(client: Client = Depends(get_available_client)):
    """Return client data"""
    return client
