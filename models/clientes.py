import ttkbootstrap as tb
from ttkbootstrap.constants import *

from controle.conexao import Conexao
from models.pessoas import Pessoa


class Cliente(Pessoa):
   
    def __init__(self, nome, pessoa, cnpj_cpf, rg_ie, tel,email,ender,
                bairro, cidade, uf, ativo,data_cad):
        super().__init__(nome, pessoa, cnpj_cpf, rg_ie, tel,email,ender,
                bairro, cidade, uf, ativo,data_cad)