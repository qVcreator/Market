from typing import List

from fastapi import APIRouter, Depends, status

from Market import models
from Market.services.role import RoleChecker
from Market.services.transaction import TransactionService

router = APIRouter(
    prefix="/transactions",
    tags=['transactions']
)


@router.get(
    '/{transaction_id}',
    status_code=status.HTTP_200_OK,
    response_model=models.ShowTransaction
)
async def get_transaction_by_id(
        transaction_id: int,
        current_user: models.AuthUser = Depends(RoleChecker([
            models.Role.USER,
            models.Role.ADMIN
        ])),
        transaction_service: TransactionService = Depends()
):
    return await transaction_service.get_transaction_by_id(transaction_id)


@router.get(
    '/all/',
    status_code=status.HTTP_200_OK,
    response_model=List[models.ShowTransaction]
)
async def get_all_transactions_by_user_id(
        current_user: models.AuthUser = Depends(RoleChecker([
            models.Role.USER
        ])),
        transaction_service: TransactionService = Depends()
):
    return await transaction_service.get_all_transactions_by_user_id(current_user.id)
