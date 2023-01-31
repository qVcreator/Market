from typing import List

from asyncpg import Type
from fastapi import Depends

from Market import models, tables
from Market.dal.user import UserDal
from Market.models import Token
from Market.services.auth import AuthService


class UserService:
    def __init__(
            self,
            auth_service: AuthService = Depends(),
            user_dal: UserDal = Depends()
    ):
        self.user_dal = user_dal
        self.auth_service = auth_service

    async def register_new_user(
            self,
            user_data: models.CreateUser,
    ) -> Token:
        user = tables.User(
            email=user_data.email,
            first_name=user_data.first_name,
            second_name=user_data.second_name,
            father_name=user_data.first_name,
            role=models.Role.USER,
            password=self.auth_service.hash_password(user_data.password),
        )

        await self.user_dal.create_user(user)

        return self.auth_service.create_token(user)

    async def delete_user(self, user_id: int):
        await self.user_dal.delete_user(user_id)

    async def get_all_users(self) -> List[tables.User]:
        return await self.user_dal.get_all_users()

    async def get_user_by_id(self, user_id: int) -> tables.User:
        return await self.user_dal.get_user_by_id(user_id)
