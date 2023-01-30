from decimal import Decimal

from pydantic import BaseModel


class ShowAccount(BaseModel):
    balance: Decimal

    class Config:
        orm_mode = True
