from fastapi import FastAPI
from app.api import clientes

app = FastAPI(title="Sistema Mecânica")

app.include_router(clientes.router, prefix="/clientes", tags=["Clientes"])