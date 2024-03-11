from fastapi import HTTPException
from starlette import status

from app.account.models import User
from app.account.services import make_encrypted
from app.utils import generate_random_string

from .models import Client
from .schemas import ClientPayload

async def register_client(creator: User, dto: ClientPayload) -> Client:
    """Register new client and return client_secret_plain (only once)"""
    client_secret_plain: str = generate_random_string(32)
    client: Client = await Client.create(**dto.model_dump(),
                                         client_id=generate_random_string(32),
                                         client_secret=make_encrypted(client_secret_plain),
                                         owner=creator)
    client.client_secret = client_secret_plain
    return client


async def get_client_by_id(client_id: str) -> Client:
    client = await Client.filter(client_id=client_id).first()
    if client is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return client


async def update_client(client: Client, dto: ClientPayload) -> Client:
    client = client.update_from_dict(dto.model_dump())
    await client.save()
    return client
