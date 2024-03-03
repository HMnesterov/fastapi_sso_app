from pydantic import BaseModel, Field, EmailStr
from tortoise.contrib.pydantic import pydantic_model_creator

from .models import User


class UserCreatePayload(BaseModel):
    email: EmailStr
    first_name: str = Field(min_length=1)
    last_name: str = Field(min_length=1)
    password: str = Field(min_length=8)


class UserAuthPayload(BaseModel):
    email: EmailStr
    password: str


UserResponse = pydantic_model_creator(User, exclude=("hashed_password", "id"))
