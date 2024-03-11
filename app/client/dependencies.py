from fastapi import Depends, HTTPException
from starlette import status

from app.client.models import Client
from app.account.dependencies import get_session_user
from app.account.models import User
from . import services as client_service


async def get_valid_client(client_id: str) -> Client:
    """Get client by id """
    return await client_service.get_client_by_id(client_id)


async def get_available_client(client: Client = Depends(get_valid_client),
                               user: User = Depends(get_session_user)) -> Client:
    if client.owner_id != user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return client
