from datetime import datetime

from pydantic import BaseModel


class WalletRequest(BaseModel):
    address: str

class WalletResponse(BaseModel):
    address: str
    balance: float
    bandwidth: int
    energy: int

class WalletQueryOut(BaseModel):
    address: str
    bandwidth: int
    energy: int
    balance: float
    date_added: datetime
