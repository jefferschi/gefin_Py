import ttkbootstrap as tb
from ttkbootstrap.constants import *

from models.pessoas import Pessoa


class Fornecedor(Pessoa):
       
    def __init__(self, nome, pessoa, cnpj_cpf, rg_ie, tel,email,ender,
                bairro, cidade, uf, ativo, data_cad):
        super().__init__(nome, pessoa, cnpj_cpf, rg_ie, tel,email,ender,
                bairro, cidade, uf, ativo, data_cad)

