from sqlalchemy import Column, Integer, String, Boolean, Column, DateTime, Integer, String
from datetime import datetime
from ..database import Base

class Fletero(Base):
    __tablename__ = "fleteros"

    id = Column(Integer, primary_key=True)
    cuit = Column(String, unique=True)
    razon_social = Column(String(150), nullable=False)
    cuit = Column(String(11), unique=True, nullable=False)
    provincia_id = Column(Integer, nullable=False)
    localidad_id = Column(Integer, nullable=False)
    direccion = Column(String(200))
    cpostal = Column(String(10))
    activo = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )