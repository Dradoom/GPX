from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from database import Base

class Vehicle(Base):
    __tablename__ = 'vehicle'
    fzid = Column(Integer, primary_key=True,autoincrement=True)
    polkz = Column(String(128))
    fahrgestellnummer = Column(String(128))

    def __init__(self, polkz, fahrgestellnummer):
        self.polkz = polkz
        self.fahrgestellnummer = fahrgestellnummer