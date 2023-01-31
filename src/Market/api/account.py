from typing import List

from fastapi import APIRouter, status, Depends

from Market import models
from Market.services.account import AccountService
from Market.services.role import RoleChecker

router = APIRouter(
    prefix="/accounts",
    tags=['accounts']
)


@router.get(
    '/all/',
    status_code=status.HTTP_200_OK,
    response_model=List[models.ShowAccount]
)
async def get_all_accounts(
        account_service: AccountService = Depends(),
        current_user: models.AuthUser = Depends(RoleChecker([
            models.Role.USER,
        ]))
):
    return await account_service.get_all_users_account(current_user.id)


@router.get(
    '/{account_id}',
    status_code=status.HTTP_200_OK,
    response_model=models.ShowAccount
)
async def get_account_by_id(
        account_id: int,
        account_service: AccountService = Depends(),
        current_user: models.AuthUser = Depends(RoleChecker([
            models.Role.USER,
            models.Role.ADMIN
        ]))
):
    return await account_service.get_account(current_user.id, account_id)


@router.get(
    '/user/{user_id}',
    status_code=status.HTTP_200_OK,
    response_model=List[models.ShowAccount]
)
async def get_all_accounts_by_user_id(user_id: int):
    pass
