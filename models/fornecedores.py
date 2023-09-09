import ttkbootstrap as tb
from ttkbootstrap.constants import *

from clientes import Cliente

# colocar as classes que estruturam os dados e conectam com o banco de dados
# criar o banco de dados diretamento no SQLiteStudio ou similar, não criar no código python

class Fornecedor(Cliente):    
    def __init__(self, nome=None, pessoa=None, cnpj_cpf=None, rg_ie=None, tel=None,email=None,ender=None,
                bairro=None, cidade=None, uf=None, ativo=None):
        super().__init__(nome=None, pessoa=None, cnpj_cpf=None, rg_ie=None, tel=None,email=None,ender=None,
                bairro=None, cidade=None, uf=None, ativo=None)
    