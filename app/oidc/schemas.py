import datetime

from pydantic import BaseModel

from app.enums import TokenType


class TokenBaseScheme(BaseModel):
    """Base scheme for every jwt token"""
    expire_at: datetime.datetime  # datetime.iso
    token_type: str = TokenType.UNDEFINED


class TokenUserBaseScheme(TokenBaseScheme, BaseModel):
    """Base scheme for user auth using jwt"""
    user_id: int


class TokenClientBaseScheme(TokenBaseScheme, BaseModel):
    """Base client identification scheme"""
    client_id: str
    client_secret: str


class AccessTokenScheme(TokenUserBaseScheme, TokenClientBaseScheme):
    """Access token scheme"""
    token_type: str = TokenType.ACCESS


class RefreshTokenScheme(TokenClientBaseScheme, TokenUserBaseScheme):
    """Refresh token scheme"""
    token_type: str = TokenType.REFRESH


class AuthTokenScheme(TokenUserBaseScheme):
    """Auth token scheme"""
    client_id: str


class AccessTokenPayload(BaseModel):
    """User payload which is sent in order to receive access and refresh token"""
    client_id: str
    client_secret: str
    code: str


class AccessTokenResponse(BaseModel):
    """Response to obtain access and refresh jwt tokens"""
    access_token: str
    refresh_token: str
    type: str = "Bearer"
