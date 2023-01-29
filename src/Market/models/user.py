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
