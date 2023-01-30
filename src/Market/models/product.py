from decimal import Decimal

from pydantic import BaseModel


class Product(BaseModel):
    id: int
    title: str
    description: str
    price: Decimal

    class Config:
        orm_mode = True


class CreateProduct(BaseModel):
    title: str
    description: str
    price: Decimal
