from typing import Type, List

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from Market.database import get_async_session
from Market.tables import Transaction, Account


class TransactionDal:
    def __init__(
            self,
            session: AsyncSession = Depends(get_async_session)):
        self.session = session

    async def get_transaction_by_id(self, transaction_id: int) -> Type[Transaction] | None:
        return await (
            self.session
            .get(Transaction, transaction_id)
        )

    async def get_all_transactions_by_user_id(
            self,
            user_id: int
    ) -> Type[List[Transaction]]:
        query = select(Transaction)\
            .filter(Transaction.account.any(Account.user_id == user_id))

        result = await (
            self.session
            .execute(query)
        )
        return result.scalars().all()

    async def create_transaction(
            self,
            transaction_data: Transaction
    ) -> int:
        self.session.add(transaction_data)
        await self.session.commit()
        return transaction_data.id
