import datetime

from pydantic import BaseModel

from app.enums import TokenType


class TokenBaseModel(BaseModel):
    expire_at: datetime.datetime  # datetime.iso
    token_type: str = TokenType.undefined


class TokenUserBaseModel(TokenBaseModel, BaseModel):
    user_id: int


class AccessTokenPayload(BaseModel):
    client_id: str
    client_secret: str
    code: str


class AccessTokenResponse(BaseModel):
    access_token: str
    refresh_token: str


class AccessTokenScheme(TokenUserBaseModel):
    client_id: str
    client_secret: str
    token_type: str = TokenType.access


class RefreshTokenScheme(TokenUserBaseModel):
    client_id: str
    token_type: str = TokenType.refresh


class AuthTokenScheme(TokenUserBaseModel):
    client_id: str
