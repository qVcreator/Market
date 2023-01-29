from typing import Type

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from Market.database import get_async_session
from Market.tables import Transaction


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

    async def get_all_transactions(self) -> Transaction:
        query = select(Transaction)
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
