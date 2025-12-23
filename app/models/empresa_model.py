from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from ..database import Base
from datetime import datetime


class Empresa(Base):
    __tablename__ = "empresas"
    id = Column(Integer, primary_key=True, index=True)
    # Perfil de empresa:
    razon_social = Column(String(150), nullable=False)
    cuit = Column(String(11), unique=True, nullable=False)
    provincia_id = Column(Integer, ForeignKey("provincias.id"), nullable=False)
    localidad_id = Column(Integer, ForeignKey("localidades.id"), nullable=False)
    direccion = Column(String(200))
    cpostal = Column(String(10))
    activa = Column(Boolean, nullable=False, default=True)
    # Ingresos Brutos (el nro es el CUIT)
    regimen_iibb = Column(String(30))  # local, multilateral, exento.
    # Auditoría:
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )