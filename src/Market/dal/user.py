from typing import List

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..database import get_async_session
from ..tables import User


class UserDal:
    def __init__(
            self,
            session: AsyncSession = Depends(get_async_session)):
        self.session = session

    async def create_user(
            self,
            user_data: User
    ):
        self.session.add(user_data)
        await self.session.commit()

    async def delete_user(
            self,
            user_id: int
    ):
        user_to_delete = await (
            self.session
            .get(User, user_id)
        )

        user_to_delete.is_delete = True

        await self.session.commit()

    async def get_all_users(self) -> List[User]:
        query = (
            select(User)
            .filter_by(is_deleted=False)
        )
        result = await (
            self.session
            .execute(query)
        )
        return result.scalars().all()

    async def get_user_by_id(
            self,
            user_id: int):
        return await (
            self.session
            .get(User, user_id)
        )

    async def get_user_by_email(
            self,
            email: str) -> User | None:

        return await (
            self.session
            .get(User,
                 {'email': email})
        )
