from decimal import Decimal
from typing import Type, List

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from Market.database import get_async_session
from Market.tables import Account


class AccountDal:
    def __init__(
            self,
            session: AsyncSession = Depends(get_async_session)):
        self.session = session

    async def get_account(
            self,
            account_id: int
    ) -> Type[Account] | None:
        account = await (
            self.session
            .get(Account, account_id)
        )

        return account

    async def get_all_users_account(
            self,
            user_id: int
    ) -> Type[List[Account]]:
        query = select(Account).filter_by(user_id=user_id)

        accounts = await (
            self.session
            .execute(query)
        )

        return accounts.scalars().all()

    async def update_balance(
            self,
            amount: Decimal,
            account_id: int
    ):
        account = await (
            self.session
            .get(Account, account_id)
        )

        account.balance -= amount

        await self.session.commit()


