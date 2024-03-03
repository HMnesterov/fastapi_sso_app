import os
from typing import Tuple

from fastapi import HTTPException
from starlette import status

from app.account.models import User
from app.account.services import make_password
from app.oauth2.models import Client
from app.oauth2.schemas import ClientPayload
from app.utils import generate_random_string


async def register_client(creator: User, dto: ClientPayload) -> Client:
    """Register new client and return client_secret_plain (only once)"""
    client_secret_plain: str = generate_random_string(32)
    client: Client = await Client.create(**dto.model_dump(),
                                         client_id=generate_random_string(32),
                                         client_secret=make_password(client_secret_plain),
                                         owner=creator)
    client.client_secret = client_secret_plain
    return client


async def get_client(client_id: str, user: User) -> Client:
    client: Client = await Client.filter(client_id=client_id).select_related('owner').first()
    if client is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if client.owner_id != user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return client


async def update_client(client: Client, dto: ClientPayload) -> Client:
    client = client.update_from_dict(dto.model_dump())
    await client.save()
    return client
