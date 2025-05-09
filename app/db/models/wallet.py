from datetime import datetime
from sqlalchemy import Integer, String, DateTime, Float
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from app.db.session import engine

Base = declarative_base()

class Wallet(Base):
    __tablename__ = 'wallets'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    address: Mapped[str] = mapped_column(String, autoincrement=False)
    balance: Mapped[float] = mapped_column(Float, autoincrement=False)
    bandwidth: Mapped[int] = mapped_column(Integer, autoincrement=False)
    energy: Mapped[int] = mapped_column(Integer, autoincrement=False)
    date_added: Mapped[datetime] = mapped_column(DateTime, autoincrement=False)

Base.metadata.create_all(bind=engine)