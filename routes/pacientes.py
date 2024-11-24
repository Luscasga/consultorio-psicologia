from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import SessionLocal
from models.paciente import Paciente

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def listar_pacientes(db: Session = Depends(get_db)):
    return db.query(Paciente).all()

@router.post("/")
def criar_paciente(nome: str, email: str, telefone: str, db: Session = Depends(get_db)):
    novo_paciente = Paciente(nome=nome, email=email, telefone=telefone)
    db.add(novo_paciente)
    db.commit()
    return {"message": "Paciente criado com sucesso"}
