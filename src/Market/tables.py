from datetime import datetime

from sqlalchemy.sql import functions
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    DECIMAL,
    ForeignKey
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    second_name = Column(String, nullable=False)
    father_name = Column(String)
    date_create = Column(DateTime(timezone=True), server_default=functions.now())
    date_update = Column(DateTime(timezone=True), onupdate=functions.now())
    is_deleted = Column(Boolean, default=False)


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(DECIMAL, nullable=False)
    is_deleted = Column(Boolean, default=False)


class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    balance = Column(DECIMAL, nullable=False, default=0)

    user = relationship("User", backref='account')


class Transaction(Base):
    __tablename__ = 'transaction'
    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey("account.id"))
    amount = Column(DECIMAL, nullable=False)

    account = relationship("Account", backref='transaction')
