from sqlalchemy import Column, Integer, Boolean, DateTime, ForeignKey
from ..database import Base
from datetime import datetime


class FlotaFletero(Base):
    __tablename__ = "flota_fleteros"

    id = Column(Integer, primary_key=True, index=True)

    fletero_id = Column(Integer, ForeignKey("fleteros.id"), nullable=False)

    activo = Column(Boolean, nullable=False, default=True)
    verificado = Column(Boolean, nullable=False, default=False)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
