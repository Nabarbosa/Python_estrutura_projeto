from atividade1.models.enums.unidade_federativa import Unidade_Federativa

class Endereco:
    def __init__(self, logadouro: str, numero: str, complemento: str, cep: str, cidade: str, uf: Unidade_Federativa) -> None:
        self.logadouro = logadouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        self.uf = uf

    def __str__(self) -> str:
        return(f"\n== Endereço =="
               f"\nLogadouro: {self.logadouro}"
               f"\nNúmero: {self.numero}"
               f"\nComplemento: {self.complemento}"
               f"\nCEP: {self.cep}"
               f"\nCidade: {self.cidade}"
               f"\nUF: {self.uf.texto} / {self.uf.sigla}"
               f"\n======================================")
