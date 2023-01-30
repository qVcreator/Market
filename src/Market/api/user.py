from fastapi import APIRouter, status, Depends
from fastapi.security import OAuth2PasswordRequestForm

from .. import models
from ..services.auth import AuthService
from ..services.user import UserService
from ..services.role import RoleChecker

router = APIRouter(
    prefix="/users",
    tags=['users']
)


@router.post(
    '/sign-up/',
    status_code=status.HTTP_201_CREATED,
    response_model=models.Token
)
async def sign_up(
        user_data: models.CreateUser,
        user_service: UserService = Depends()
):
    return await user_service.register_new_user(user_data)


@router.post(
    '/sign-in/',
    status_code=status.HTTP_200_OK,
    response_model=models.Token
)
async def sign_in(
        auth_data: OAuth2PasswordRequestForm = Depends(),
        auth_service: AuthService = Depends()
):
    return await auth_service.authenticate_user(
        auth_data.username,
        auth_data.password,
    )
