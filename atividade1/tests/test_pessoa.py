import pytest

from atividade1.models.pessoa import Pessoa # Caminho relativo
from atividade1.models.endereco import Endereco # Caminho Absoluto
from atividade1.models.enums.sexo import Sexo
from atividade1.models.enums.unidade_federativa import Unidade_Federativa

#Modelo.
@pytest.fixture
def criar_pessoa():
    primeira_pessoa = Pessoa(123, "Tainá", "14/03/2006", "71 96789-5436", "taina@gmail.com", Sexo.FEMININO, 
                         Endereco("Rua A", "15", "N/D", "5673932", "Cidade A", Unidade_Federativa.BAHIA))
    return primeira_pessoa

def test_pessoa_id(criar_pessoa):
    assert criar_pessoa.id == 123

def test_pessoa_nome(criar_pessoa):
    assert criar_pessoa.nome == "Tainá"

def test_pessoa_data_nascimento(criar_pessoa):
    assert criar_pessoa.dataDeNascimento == "14/03/2006"
