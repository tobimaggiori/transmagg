from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, ForeignKey
from ..database import Base
from datetime import datetime


class FlotaUnidad(Base):
    __tablename__ = "flota_unidades"

    id = Column(Integer, primary_key=True, index=True)

    flota_id = Column(Integer, ForeignKey("flota_fleteros.id"), nullable=False)

    tipo_unidad = Column(String(20), nullable=False)  # camion | tractor | acoplado | semirremolque
    patente = Column(String(10), unique=True, nullable=False)

    ruta_vencimiento = Column(Date, nullable=True)
    vtv_vencimiento = Column(Date, nullable=True)
    seguro_vencimiento = Column(Date, nullable=True)

    verificado = Column(Boolean, nullable=False, default=False)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
