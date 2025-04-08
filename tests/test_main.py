from datetime import datetime

from fastapi.testclient import TestClient
from app.main import app
from app.db.models.wallet import Wallet


def test_wallet_insert():
    from app.db.session import get_db
    db = next(get_db())
    record = Wallet(address="TXYZ123", bandwidth=100, energy=200, balance=300.5, date_added=datetime.now())
    db.add(record)
    db.commit()
    found = db.query(Wallet).filter(Wallet.address == "TXYZ123").first()
    assert found is not None
    assert found.balance == 300.5

def test_get_wallets_endpoint():
    client = TestClient(app)
    response = client.get("/wallets")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
