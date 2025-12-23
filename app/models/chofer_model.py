from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from ..database import Base
from datetime import datetime


class Chofer(Base):
    __tablename__ = "choferes"

    id = Column(Integer, primary_key=True, index=True)

    fletero_id = Column(Integer, ForeignKey("fleteros.id"), nullable=False) # Para vincular al fletero propietario.
    flota_id = Column(Integer, ForeignKey("flota_fleteros.id"), nullable=False) # Para asignarle chasis y acoplado.

    nombres = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    cuit = Column(String(11), unique=True, nullable=False)

    activo = Column(Boolean, nullable=False, default=True)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
