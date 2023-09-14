from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from database import Base

class Track(Base):
    __tablename__ = 'track'
    tid = Column(Integer, primary_key=True, autoincrement=True)
    dateiname = Column(String(128))
    pid = Column(Integer, ForeignKey('person.pid'),nullable=False)
    fzid = Column(Integer, ForeignKey('vehicle.fzid'),nullable=False)

    def __init__(self, dateiname, person, vehicle):
        self.dateiname = dateiname
        self.pid = person.pid
        self.fzid = vehicle.fzid