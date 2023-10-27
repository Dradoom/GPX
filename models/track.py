from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from database import Base

class Track(Base):
    __tablename__ = 'track'
    tid = Column(Integer, primary_key=True, autoincrement=True)
    dateiname = Column(String(128))
    name = Column(String(128))
    pid = Column(Integer, ForeignKey('person.pid'),nullable=False)
    fzid = Column(Integer, ForeignKey('vehicle.fzid'),nullable=False)

    def __init__(self, dateiname, person, vehicle, name):
        self.dateiname = dateiname
        self.name = name
        self.pid = person.pid
        self.fzid = vehicle.fzid        