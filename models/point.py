
from sqlalchemy import Column, DateTime, Float, Integer, String, ForeignKey, Boolean
from database import Base

class Point(Base):
    __tablename__ = 'point'
    ptid = Column(Integer, primary_key=True, autoincrement=True)
    lat = Column(Float)
    lon = Column(Float)
    ele = Column(Float)
    dt = Column(DateTime(timezone=True))
    tid = Column(Integer, ForeignKey('track.tid'),nullable=False)