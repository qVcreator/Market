from typing import Type, List

from fastapi import Depends

from Market import models, tables
from Market.dal.transaction import TransactionDal
from Market.services.account import AccountService
from Market.tables import Transaction


class TransactionService:
    def __int__(
            self,
            transaction_dal: TransactionDal = Depends()):
        self.transaction_dal = transaction_dal

    async def get_transaction_by_id(self, transaction_id: int) -> Type[Transaction]:
        return await self.transaction_dal.get_transaction_by_id(transaction_id)

    async def get_all_transactions_by_user_id(
            self,
            user_id: int
    ) -> Type[List[Transaction]]:
        return await self.transaction_dal.get_all_transactions_by_user_id(user_id)

    async def create_transaction(
            self,
            transaction_data: models.transaction
    ) -> int:
        new_transaction = tables.Transaction(**transaction_data)
        return await self.transaction_dal.create_transaction(new_transaction)
