from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field
from dataclasses import dataclass
from typing import Optional
from datetime import datetime

""" Funciones claves de BaseModel
Validación de Tipos: Si tú definiste que fletero_id es un int y alguien manda el texto "cuarenta",
BaseModel lanza un error automáticamente y le avisa al usuario: "Eh, esto tiene que ser un número".

Conversión de Datos (Parsing): Si alguien manda el CUIT como un número 20304050607, 
BaseModel lo convierte automáticamente a str (texto) si así lo definiste.

Serialización a JSON: Es lo que permite que tu servidor hable con el dispositivo/web. 
BaseModel sabe cómo transformar la clase de Python a un formato que la App/web entienda perfectamente.


Es común confundirse entre los dos tipos de "Modelos" que vamos a usar:
Modelos de SQLAlchemy: Son para la Base de Datos (lo que se guarda en el disco de tu Debian).
Modelos de Pydantic (BaseModel): Son para el Intercambio de Datos (lo que viaja por internet entre la App y tu servidor).
En resumen: BaseModel es el "guardia de seguridad" de tu sistema. 
Revisa que todo lo que entra por los formularios de registro o carga de viajes sea válido según las reglas que tú definas.
"""


# La siguiente clase representa a un usuario ya registrado.
@dataclass #decorador de Python que ahorra __init__(self, ...)
class Usuario():
    id: int
    email: str
    nombre: str
    celular: str
    rol: str

    # Login sin contraseña:
    codigo_acceso: Optional[str] = None
    codigo_vencimiento: Optional[datetime] = None

    # Relaciones:
    fletero_id: Optional[int] = None
    empresa_id: Optional[int] = None
    chofer_id: Optional[int] = None

"""
Existirá una clase diferente para el registro de un usuario
es por ello que esta clase no tiene CUIT, cuando un usuario se
registre, ingresara su CUIT y el sistema buscara ese CUIT en cada
una de las tablas de fletero, empresa, chofer, y luego completara
esta clase con el id correspondiente en fletero_id, empresa_id, chofer_id.
Si un usuario es solamente fletero, entonces los demas id quedan en vacios.
"""

class Registro(BaseModel):
    nombre_completo: str = Field(...,min_length=3, max_length=50) #... indica que el campo es obligatorio
    email: EmailStr
    celular: str = Field(..., min_length=10, max_length=15)
    cuit: str = Field(min_length=11, max_length=11) # CUIT que lo asocia con transmagg. (Empresa, Chofer, Fletero)