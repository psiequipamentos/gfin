from datetime import datetime
import enum
from sqlalchemy import Column, DateTime, Enum, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class AccountType(str, enum.Enum):
    personal = "personal"
    company = "company"


class CategoryType(str, enum.Enum):
    income = "income"
    expense = "expense"


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    type = Column(Enum(AccountType), nullable=False)
    balance = Column(Float, default=0)

    transactions = relationship(
        "Transaction",
        back_populates="account_origin",
        foreign_keys="Transaction.account_origin_id",
    )


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    type = Column(Enum(CategoryType), nullable=False)


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    description = Column(String, nullable=True)
    category_id = Column(Integer, ForeignKey("categories.id"))
    account_origin_id = Column(Integer, ForeignKey("accounts.id"))
    account_dest_id = Column(Integer, ForeignKey("accounts.id"), nullable=True)

    category = relationship("Category")
    account_origin = relationship(
        "Account", foreign_keys=[account_origin_id], back_populates="transactions"
    )
    account_dest = relationship("Account", foreign_keys=[account_dest_id])
