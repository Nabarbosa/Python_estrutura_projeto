import pytest

from meu_projeto.models.pessoa import Pessoa
from meu_projeto.models.endereco import Endereco
from meu_projeto.models.enums.sexo import Sexo

#Modelo.
@pytest.fixture
def criar_pessoa():
    pessoa_1 = Pessoa("Marta", 22, Sexo.FEMININO, Endereco("Rua A", 11))
    return pessoa_1

def test_pessoa_valido(criar_pessoa):
    assert criar_pessoa.idade == 22

def test_pessoa_valido(criar_pessoa):
    assert criar_pessoa.nome == "Marta"
