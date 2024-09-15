import os

from models.pessoa import Pessoa
from models.endereco import Endereco
from models.enums.sexo import Sexo
from models.enums.unidade_federativa import Unidade_Federativa

os.system("cls || clear")

#Instaciando Classes
primeira_pessoa = Pessoa(123, "Tainá", "14/03/2006", "71 96789-5436", "taina@gmail.com", Sexo.FEMININO, 
                         Endereco("Rua A", "15", "N/D", "5673932", "Cidade A", Unidade_Federativa.BAHIA))


print(primeira_pessoa)