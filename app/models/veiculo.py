from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class Veiculo(Base):
    __tablename__='veiculos'
    id = Column(Integer, primary_key=True, index=True)
    modelcar = Column(String(120), nullable=False)
    placa = Column(String(10), unique=True, nullable=False)
    client_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    cliente = relationship("Cliente", back_populates="veiculos")
    