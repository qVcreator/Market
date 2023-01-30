from decimal import Decimal

from pydantic import BaseModel


class CreateTransaction(BaseModel):
    account_id: int
    amount: Decimal


class ShowTransaction(BaseModel):
    account_id: int
    amount: Decimal

    class Config:
        orm_mode = True
