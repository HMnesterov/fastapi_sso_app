import datetime

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from .models import Client
from app.account.schemas import UserResponse

ClientPayload = pydantic_model_creator(Client, exclude=("client_id", "client_secret", "created_at"))


class ClientResponse(BaseModel):
    name: str
    homepage: str
    callback_url: str
    created_at: datetime.datetime
    owner: UserResponse
    client_id: str


class ClientCreateResponse(ClientResponse):
    client_secret: str

