from decimal import Decimal
from typing import Type

from fastapi import Depends, HTTPException, status

from Market import models
from Market.dal.account import AccountDal
from Market.services.transaction import TransactionService
from Market.tables import Account


class AccountService:
    def __init__(self,
                 account_dal: AccountDal = Depends(),
                 transaction_service: TransactionService = Depends()):
        self.transaction_service = transaction_service
        self.account_dal = account_dal

    async def get_account_balance(
            self,
            crnt_user_id: int,
            account_id: int
    ):
        account = await self.get_account(crnt_user_id, account_id)

        return account.balance

    async def get_account(
            self,
            crnt_user_id: int,
            account_id,
    ) -> Type[Account]:
        account = await self.account_dal.get_account(account_id)

        if account is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        if account.user_id != crnt_user_id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)

        return account

    async def get_all_users_account(self, user_id: int):
        return await self.account_dal.get_all_users_account(user_id)

    async def update_account_balance(
            self,
            amount: Decimal,
            account_id: int
    ):
        new_transaction = models.CreateTransaction(
            account_id=account_id,
            amount=amount
        )
        await self.transaction_service.create_transaction(new_transaction)
        await self.account_dal.update_balance(amount, account_id)

