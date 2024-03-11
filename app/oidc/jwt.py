from typing import TypeVar

from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from starlette import status
from app.utils import now
from core.settings import settings
from .schemas import TokenBaseScheme

base_token_scheme = TypeVar(name="base_token_scheme", bound=TokenBaseScheme)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_jwt_token(token_data: base_token_scheme) -> str:
    """Generate new jwt token based on provided data"""
    # expire time of the token
    to_dict: dict = token_data.model_dump()
    to_dict['expire_at'] = token_data.expire_at.isoformat()

    encoded_jwt = jwt.encode(to_dict,
                             key=settings.SECRET_KEY,
                             algorithm=settings.ALGORITHM)

    # return the generated token
    return encoded_jwt


def decode_jwt_token(token: str) -> dict:
    """Get jwt token data"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"})
    try:
        token_data = jwt.decode(token=token, key=settings.SECRET_KEY, algorithms=settings.ALGORITHM)
        if now().fromisoformat(token_data['expire_at']) < now():
            raise credentials_exception
        return token_data
    except JWTError:
        raise credentials_exception
