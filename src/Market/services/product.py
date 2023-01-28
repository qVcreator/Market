from fastapi import Depends
from sqlalchemy.orm import Session

from ..models import *
from ..dependencies import *


class ProductService:
    def __init__(
            self,
            product_dal: ProductDal = Depends(get_product_dal)):
        self.product_dal = product_dal

    async def get_all_products(self):
        return await self.product_dal.get_all_products()

    async def get_product(self, product_id: int):
        return await self.product_dal.get_product(product_id)

    async def create_product(self, product_data: CreateProduct):
        return await self.product_dal.create_product(product_data)
