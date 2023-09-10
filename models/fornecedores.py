import ttkbootstrap as tb
from ttkbootstrap.constants import *

from models.pessoas import Pessoa

# colocar as classes que estruturam os dados e conectam com o banco de dados
# criar o banco de dados diretamento no SQLiteStudio ou similar, não criar no código python

class Fornecedor(Pessoa):
    
    def __init__(self, nome, pessoa, cnpj_cpf, rg_ie, tel,email,ender,
                bairro, cidade, uf, ativo):
        super().__init__(nome, pessoa, cnpj_cpf, rg_ie, tel,email,ender,
                bairro, cidade, uf, ativo)
    