from decimal import Decimal

from fastapi import APIRouter, status, Depends

from Market import models
from Market.services.account import AccountService
from Market.services.role import RoleChecker

router = APIRouter(
    prefix="/payment",
    tags=['payment']
)


@router.post(
    '/webhook',
    status_code=status.HTTP_200_OK
)
async def deposit(
        amount: Decimal,
        account_id: int,
        current_user: models.AuthUser = Depends(RoleChecker([
            models.Role.USER,
        ])),
        account_service: AccountService = Depends()
):
    await account_service.update_account_balance(amount, account_id)
