from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
# El .. le dice a Python: "Anta atrás una carpeta y buscá database.py"
from ..database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    nombre = Column(String)
    celular = Column(String)
    rol = Column(String, default="usuario")
    activo = Column(Boolean, default=True)

    # Login sin contrasena
    codigo = Column(String, nullable=True)
    tiempo = Column(DateTime, nullable=True)

    # Relaciones
    fletero_id = Column(Integer, ForeignKey("fleteros.id"), nullable=True)
 #   empresa_id = Column(Integer, ForeignKey("empresas.id"), nullable=True)
 #   chofer_id = Column(Integer, ForeignKey("choferes.id"), nullable=True)

    def vincular_fletero():
        None
    def vincular_empresa():
        None
    def vincular_chofer():
        None
