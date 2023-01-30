from fastapi import APIRouter, Depends, status

from Market import models
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
        transaction_service: TransactionService = Depends()
):
    return await transaction_service.get_transaction_by_id(transaction_id)
