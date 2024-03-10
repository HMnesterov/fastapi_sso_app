from fastapi import APIRouter, Response, Depends

from . import services as acc_service
from .dependencies import get_current_user
from .models import User
from .schemas import UserCreatePayload, UserResponse, UserAuthPayload
from .sessions import add_session

router = APIRouter()


@router.post("/register", response_model=UserResponse, status_code=201)
async def create_account(response: Response, user_payload: UserCreatePayload) -> UserResponse:
    """Create new account and set session"""
    user: User = await acc_service.create_user(dto=user_payload)
    await add_session(response, user)
    return user


@router.post("/login", response_model=UserResponse, status_code=200)
async def login(response: Response, user_auth_payload: UserAuthPayload) -> UserResponse:
    """Do log_in"""
    user: User = await acc_service.get_user(dto=user_auth_payload)
    await add_session(response, user)
    return user


@router.get("/me", response_model=UserResponse)
async def get_user_info(user: User = Depends(get_current_user)) -> UserResponse:
    """Receive information about user"""
    return user
