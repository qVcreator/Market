from typing import List, Type

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .. import tables, models
from ..database import get_async_session
from ..tables import Product


class ProductDal:
    def __init__(
            self,
            session: AsyncSession = Depends(get_async_session)):
        self.session = session

    async def get_all_products(self) -> List[Product]:
        query = select(Product)
        result = await (
            self.session
            .execute(query)
        )
        return result.scalars().all()

    async def get_product(self, product_id: int) -> Type[Product] | None:
        return await (
            self.session
            .get(Product, product_id)
        )

    async def create_product(self, new_product: models.CreateProduct) -> int:
        product = tables.Product(**new_product.dict())
        self.session.add(product)
        await self.session.commit()
        return product.id


