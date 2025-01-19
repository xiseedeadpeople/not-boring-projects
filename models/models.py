from sqlalchemy import Column, Integer, String, Float, Date, Time
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Flight(Base):
    __tablename__ = "flights"
    id = Column(Integer, primary_key=True, autoincrement=True)
    from_city = Column(String, nullable=False)
    to_city = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    price = Column(Float, nullable=False)
