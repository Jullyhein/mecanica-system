from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.client import ClienteCreate
from app.services.importar_clientes import importar
from app.services.google_sheets import ler_google_sheets
from app.db.session import get_db
from app.models.clientes import Cliente
from app.models.veiculo import Veiculo


router = APIRouter()

GOOGLE_SHEETS_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSi4kXommAK3RPjvot8IKMWUzoH9bRLRxw48KZ4qjCyaIJam2Y_O5MvcJPx5Dxds6cmb-fEDtot6NIU/pub?output=csv"

@router.post("/importar-clientes")
def importar_clientes(db:Session = Depends(get_db)):
    importar(db)
    return {"msg": "Clientes importados com sucesso"}