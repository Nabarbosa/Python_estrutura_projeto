class Endereco:
    def __init__(self, logadouro:str, numero:int) -> None:
        self.logadouro = logadouro
        self.numero = numero

    def __str__(self) -> str:
        return(f"\nLogadouro: {self.logadouro}"
               f"\nNúmero: {self.numero}")
        