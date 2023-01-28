from fastapi import Depends, HTTPException, status

from ..dal.product import ProductDal
from ..models import *


class ProductService:
    def __init__(
            self,
            product_dal: ProductDal = Depends()):
        self.product_dal = product_dal

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
