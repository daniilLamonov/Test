from datetime import datetime
from sqlalchemy.orm import Session
from app.db.models.wallet import Wallet

def create_wallet_query(db: Session, **kwargs) -> Wallet:
    request_time = datetime.utcnow()
    new_query = Wallet(**kwargs, date_added=request_time)
    db.add(new_query)
    db.commit()
    return new_query