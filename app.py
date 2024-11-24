from fastapi import FastAPI
from routes import pacientes, consultas

app = FastAPI()

# Rotas
app.include_router(pacientes.router, prefix="/pacientes", tags=["Pacientes"])
app.include_router(consultas.router, prefix="/consultas", tags=["Consultas"])

@app.get("/")
def root():
    return {"message": "Bem-vindo ao Consultório de Psicologia API"}
