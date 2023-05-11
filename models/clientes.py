import ttkbootstrap as tb
from ttkbootstrap.constants import *

"""  Orientações para criação e uso da classe

# Exemplo: atribuição direta dos atributos individuais
# self.codigo = self.atributos['codigo']
# self.nome = self.atributos['nome']
# self.cpf = self.atributos['cpf']
# ...

# Ou, se preferir, pode acessar os atributos diretamente pelo dicionário:
# Exemplo: self.atributos['codigo'], self.atributos['nome'], self.atributos['cpf'], ...
"""

class Cliente:
   
    def __init__(self, *args):
        self.atributos = {
            'codigo': None,
            'nome': None,
            'cnpj_cpf': None,
            'rg_ie': None,
            'telefone': None,
            'email': None,
            'endereco': None,
            'bairro': None,
            'cidade': None,
            'uf': None,
            'ativo':None
        }

        if len(args) > len(self.atributos):
            raise ValueError("Número inválido de argumentos")

        for i, arg in enumerate(args):
            atributo = list(self.atributos.keys())[i]
            self.atributos[atributo] = arg


    def incluir(self):
        # teste para instanciar a classe

        cod = input('cod: ')
        nome = input('nome: ')
        cpf = input('cpf: ')

        cliente = Cliente(cod,nome,cpf)

        print(cliente.atributos['codigo'])
        print(cliente.atributos['nome'])
        print(cliente.atributos['cnpj_cpf'])

c = Cliente()
c.incluir()