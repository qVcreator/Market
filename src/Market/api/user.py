from typing import List

from fastapi import APIRouter, status, Depends, HTTPException
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


@router.get(
    '/all/',
    status_code=status.HTTP_200_OK,
    response_model=List[models.ShowUser]
)
async def get_all_users(
        current_user: models.AuthUser = Depends(RoleChecker([
            models.Role.ADMIN
        ])),
        user_service: UserService = Depends()
):
    return await user_service.get_all_users()


@router.get(
    '/{user_id}',
    status_code=status.HTTP_200_OK,
    response_model=models.ShowUser
)
async def get_user_by_id(
        user_id: int,
        current_user: models.AuthUser = Depends(RoleChecker([
            models.Role.ADMIN,
            models.Role.USER
        ])),
        user_service: UserService = Depends()
):
    if current_user.id != user_id and current_user.role is not models.Role.ADMIN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)

    return await user_service.get_user_by_id(user_id)


@router.delete(
    '/{user_id}',
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_user_by_id(
        user_id: int,
        current_user: models.AuthUser = Depends(RoleChecker([
            models.Role.ADMIN
        ])),
        user_service: UserService = Depends()
):
    return await user_service.delete_user(user_id)
