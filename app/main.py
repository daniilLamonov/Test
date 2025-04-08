from typing import List

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.db.models.wallet import Wallet
from app.schemas import WalletRequest, WalletResponse, WalletQueryOut
from app.services import get_wallet_info
from app.db.session import get_db
from app.crud import create_wallet_query

app = FastAPI()

@app.post('/wallets/add', tags=['wallet'], response_model=WalletResponse)
def get_wallet(wallet_adrees: WalletRequest, db: Session = Depends(get_db)):
    wallet_data = get_wallet_info(wallet_adrees.address)
    db_query = create_wallet_query(db, **wallet_data)
    return WalletResponse(address=db_query.address,
                          balance=db_query.balance,
                          bandwidth=db_query.bandwidth,
                          energy=db_query.energy)

@app.get("/wallets", tags=['wallet'], response_model=List[WalletQueryOut])
def list_wallets(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Wallet).order_by(Wallet.date_added.desc()).offset(skip).limit(limit).all()
