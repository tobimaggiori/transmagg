# app/main.py
from fastapi import FastAPI, Depends
# Usamos el punto para decir "está acá al lado mío"
from .database import SessionLocal, engine, Base
from sqlalchemy.orm import Session
# Importamos el CONTENIDO de la carpeta models
from . import models

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "Servidor andando y Base de Datos conectada"}

@app.get("/usuarios-db")
def obtener_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(models.Usuario).all()
    return usuarios