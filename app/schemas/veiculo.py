from pydantic import BaseModel, Field

class VeiculoCreate(BaseModel):
    modelo: str = Field(...,example="Gol 1.6")
    placa: str = Field(..., example="abc1d23")
    servico: str = Field(...,example="Manutenção")
    
