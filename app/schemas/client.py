from pydantic import BaseModel, Field, EmailStr
from typing import List
from .veiculo import VeiculoCreate



class ClienteCreate(BaseModel):
    nome_completo: str = Field(..., example="Jullyen Soares")
    telefone: str = Field(...,example="11999999999")
    cpf: str = Field(...,example="000.000.000-00")
    email: EmailStr = Field(...,example="jujuba_741@hotmail.com")
    veiculo: VeiculoCreate


class ClienteResponse(BaseModel):
    id: int
    nome_completo: set
    telefone: str
    cpf: str
    email: str

    class Config:
        from_attributes=True