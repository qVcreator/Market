from typing import List

from sqlalchemy.future import select
from sqlalchemy.orm import Session

from .. import tables
from ..tables import *


class ProductDal:
    def __init__(
            self,
            session: Session):
        self.session = session

    async def get_all_products(self) -> List[Product]:
        return await (
            self.session
            .query(Product)
            .all()
        )

    async def get_product(self, product_id: int) -> Product:
        return await (
            self.session
            .query(Product)
            .filter_by(id=product_id)
            .first()
        )

    async def create_product(self, new_product: Product) -> int:
        product = tables.Product(**new_product.dict())
        self.session.add(product)
        await self.session.flush()
        return product.id


