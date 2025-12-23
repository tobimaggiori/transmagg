from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from ..database import Base
from datetime import datetime

class Usuario(Base):
    __tablename__ = "usuarios"
    # Perfil de usuario
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), nullable=False)
    rol = Column(String(30), nullable=False)
    email = Column(String(120), unique=True, index=True, nullable=False)
    activo = Column(Boolean, nullable=False, default=True)
    # Login sin contraseña
    codigo = Column(String(80), nullable=True)
    tiempo = Column(DateTime, nullable=True)
    # Relaciones (FKs)
    fletero_id = Column(Integer, ForeignKey("fleteros.id"), nullable=True)
    empresa_id = Column(Integer, ForeignKey("empresas.id"), nullable=True)
    chofer_id = Column(Integer, ForeignKey("choferes.id"), nullable=True)
    # Auditoría
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
    def vincular_fletero():
        None
    def vincular_empresa():
        None
    def vincular_chofer():
        None
