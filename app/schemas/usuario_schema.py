from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class UsuarioBase(BaseModel):
    """
    MOLDE COMÚN (Dato Compartido):
    Define los campos básicos que cualquier usuario tiene en cualquier situación.
    Se usa como base para no repetir código en las otras clases.
    """
    email: EmailStr
    nombre: str
    celular: str

class UsuarioRegistro(UsuarioBase):
    """
    Es lo que el usuario envía al sistema para identificarse por primera vez.
    Pide el CUIT para que el sistema busque automáticamente su ficha de fletero/chofer/empresa
    Este CUIT NO se guarda en la tabla de Usuarios, solo sirve para el 'match'.
    """
    cuit: str = Field(..., min_length=11, max_length=11)

class UsuarioPublico(UsuarioBase):
    """
    PERFIL DE SALIDA (Para la App de iOS/Web):
    Esta es la 'cara visible' del usuario. Incluye el ID y los permisos (IDs de relación)
    No debe contener datos sensibles.
    """
    id: int
    rol: str
    fletero_id: Optional[int] = None
    empresa_id: Optional[int] = None
    chofer_id: Optional[int] = None

    class Config:
        # Permite transformar objetos de Base de Datos a este formato automáticamente.
        from_attributes = True