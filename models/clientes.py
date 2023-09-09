import ttkbootstrap as tb
from ttkbootstrap.constants import *

from utilitar.conexao import Conexao


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
   
    def __init__(self, nome=None, pessoa=None, cnpj_cpf=None, rg_ie=None, tel=None,email=None,ender=None,
                bairro=None, cidade=None, uf=None, ativo=None):
        
        self.nome = nome
        self.pessoa = pessoa
        self.cnpj_cpf = cnpj_cpf
        self.rg_ie = rg_ie
        self.tel = tel
        self.email = email
        self.ender = ender
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.ativo = ativo

    def incluir(self):
        conn = Conexao() # conecta ao banco de dados   
        conn.cursor.execute(""" INSERT INTO clientes (nome, pessoa, cnpj_cpf,rg_ie,telefone,email,
            endereco,bairro,cidade,uf,ativo) VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
            (self.nome,self.pessoa,self.cnpj_cpf,self.rg_ie,self.tel,self.email,self.ender,self.bairro,
             self.cidade,self.uf,self.ativo))
        conn.conex.commit() # envia as inserções para o banco
        conn.desconecta_bd()

        print("Cliente adicionado com sucesso!")
        


    def teste(self):
        # teste para instanciar a classe

        cpf = input('cpf: ')
        cod = input('cod: ')
        nome = input('nome: ')


        c1 = Cliente(nome=nome, codigo=cod, cnpj_cpf=cpf)
        print(c1.codigo)
        print(c1.cnpj_cpf)
        print(c1.nome)

        

#c = Cliente()
#c.teste()