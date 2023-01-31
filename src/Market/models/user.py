from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from ..models import Role


class User(BaseModel):
    id: int
    first_name: str
    second_name: str
    role: Role

    class Config:
        orm_mode = True


class ShowUser(BaseModel):
    email: str
    first_name: str
    second_name: str
    father_name: Optional[str]
    date_create: datetime

    class Config:
        orm_mode = True


class CreateUser(BaseModel):
    email: str
    password: str
    first_name: str
    second_name: str
    father_name: Optional[str]

    class Config:
        orm_mode = True


class AuthUser(BaseModel):
    id: int
    role: Role

    class Config:
        orm_mode = True
