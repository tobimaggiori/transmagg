from sqlalchemy import Column, Integer, String
from ..database import Base

class Fletero(Base):
    __tablename__ = "fleteros"
    id = Column(Integer, primary_key=True)
    cuit = Column(String, unique=True)