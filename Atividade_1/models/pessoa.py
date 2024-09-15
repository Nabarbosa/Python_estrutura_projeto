from models.endereco import Endereco
from models.enums.sexo import Sexo

class Pessoa:
    def __init__(self, id: int, nome: str, dataDeNascimento: str, telefone: str, email: str, sexo: Sexo, endereco: Endereco) -> None:
        self.id = id
        self.nome = nome
        self.dataDeNascimento = dataDeNascimento
        self.telefone = telefone
        self.email = email
        self.sexo = sexo
        self.endereco = endereco

    def __str__(self) -> str:
        return(f"\n== Pessoa =="
               f"\nID: {self.id}"
               f"\nNome: {self.nome}"
               f"\nData de Nascimento: {self.dataDeNascimento}"
               f"\nTelefone: {self.telefone}"
               f"\nE-mail: {self.email}"
               f"\nSexo: {self.sexo.value}"
               f"\n {self.endereco}")