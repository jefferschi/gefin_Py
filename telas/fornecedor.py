import ttkbootstrap as tb
from ttkbootstrap.constants import *

from controle.conexao import ICONE_DF
from models.fornecedores import Fornecedor

from telas.base import BaseTelaCad


"""
colocar o que seriam as views no Django, ver se precisará criar módulos.
criar arquivos separados para a interface gráfica, como cliente_interface.py, fornecedor_interface.py,
etc., onde cada arquivo contém a definição da interface gráfica para o respectivo recurso.
"""

class ForneceTelaCad(BaseTelaCad):
    def __init__(self):
        super().__init__()

class FornecTelaLista:
    def __init__(self):
        pass