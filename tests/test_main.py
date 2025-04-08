from datetime import datetime
from fastapi import HTTPException

import pytest

from app.services import get_wallet_info
from tests.conftest import client
from app.db.models.wallet import Wallet


def test_wallet_insert():
    from app.db.session import get_db
    db = next(get_db())
    query = Wallet(address="Tfdg443", bandwidth=100, energy=200, balance=300.5, date_added=datetime.now())
    db.add(query)
    db.commit()
    found = db.query(Wallet).filter(Wallet.address == "TXYZ123").first()
    assert found is not None
    assert found.balance == 300.5

def test_get_wallets_endpoint(client):
    response = client.get("/wallets", params={"limit": 1})
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 1



