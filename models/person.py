from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from database import Base

class Person(Base):
    __tablename__ = 'person'
    pid = Column(Integer, primary_key=True, autoincrement=True)
    nick = Column(String(128))
    name = Column(String(128))
    vorname = Column(String(128))
    email = Column(String(128))

    def __init__(self, nick, name, vorname, email):
        self.nick = nick
        self.name = name
        self.vorname = vorname
        self.email = email