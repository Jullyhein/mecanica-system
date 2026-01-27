from app.models.clientes import Cliente
from app.models.veiculo import Veiculo
from app.schemas.client import ClienteCreate
from app.services.google_sheets import ler_google_sheets

def importar(db):
    linhas = ler_google_sheets()
    for linha in linhas:
        cliente_schema = ClienteCreate(
            nome_completo=linha["nome completo"],
            telefone=linha["telefone"],
            cpf=linha["cpf"],
            email=linha["email"],
            veiculo={
                "modelo":linha["veiculo"],
                "placa":linha["placa"]
            }
        )
        cliente = Cliente(
            nome_completo=cliente_schema.nome_completo,
            telefone=cliente_schema.telefone,
            cpf=cliente_schema.cpf,
            email=cliente_schema.email
        )
        db.add(cliente)
        db.flush()
        veiculo = Veiculo(
            modelo=cliente_schema.veiculo.modelo,
            placa=cliente_schema.veiculo.placa,
            cliente_id=cliente.id
        )
        db.add(veiculo)
    db.commit()
    return{"status": "Importação Concluída"}