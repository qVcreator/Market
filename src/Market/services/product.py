from fastapi import Depends, HTTPException, status

from .account import AccountService
from ..dal.product import ProductDal
from ..models import *


class ProductService:
    def __init__(
            self,
            account_service: AccountService = Depends(),
            product_dal: ProductDal = Depends()):
        self.product_dal = product_dal
        self.account_service = account_service

    async def get_all_products(self):
        return await self.product_dal.get_all_products()

    async def get_product(self, product_id: int):
        product = await self.product_dal.get_product(product_id)

        if product is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product with such id doesn't exist"
            )

        return product

    async def create_product(self, product_data: CreateProduct):
        return await self.product_dal.create_product(product_data)

    async def buy_product(
            self,
            user_id: int,
            product_id: int,
            account_id: int
    ):
        product = await self.get_product(product_id)
        account = await self.account_service.get_account(user_id, account_id)

        if product.price > account.balance:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Not enough money on account with id: {account.id}"
            )

        if account.user_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN
            )

        await self.account_service.update_account_balance(product.price, account.id)
