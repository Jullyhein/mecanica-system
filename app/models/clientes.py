from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True, index=True)
    name_complete = Column(String, nullable=False)
    placa_veiculo = Column(String, nullable=False)
    phone = Column(String(20), nullable=False)
    cpf = Column(String(14))
    email = Column(String(120), unique=True, nullable=False)
    veiculos = relationship(
        "Veiculo",
        back_populates="cliente",
        cascade="all, delete-orphan"
    )