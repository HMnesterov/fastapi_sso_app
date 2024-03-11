import datetime

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from app.account.schemas import UserResponse
from .models import Client

ClientPayload = pydantic_model_creator(Client, exclude=("client_id", "client_secret", "created_at"))


class ClientResponse(BaseModel):
    """Client base response"""
    name: str
    homepage: str
    callback_url: str
    created_at: datetime.datetime
    owner: UserResponse
    client_id: str


class ClientCreateResponse(ClientResponse):
    """Client creation response only at first time in order to show client_secret"""
    client_secret: str
