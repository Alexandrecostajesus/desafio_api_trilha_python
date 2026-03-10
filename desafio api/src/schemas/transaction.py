from decimal import Decimal

from pydantic import BaseModel, condecimal

from src.enums import TransactionType


Amount = condecimal(gt=0, max_digits=10, decimal_places=2)


class TransactionIn(BaseModel):
    account_id: int
    type: TransactionType
    amount: Amount

    class Config:
        use_enum_values = True
