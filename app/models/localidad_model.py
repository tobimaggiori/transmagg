from sqlalchemy import Column, Integer, String, ForeignKey
from ..database import Base


class Localidad(Base):
    __tablename__ = "localidades"

    id = Column(Integer, primary_key=True, index=True)

    provincia_id = Column(Integer, ForeignKey("provincias.id"), nullable=False)
    nombre = Column(String(80), nullable=False)

    cp = Column(String(10))
