from .database import Base
from sqlalchemy import Column, Integer, String, Boolean


class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
