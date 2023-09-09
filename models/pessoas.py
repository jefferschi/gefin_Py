#import ttkbootstrap as tb
#from ttkbootstrap.constants import *

from utilitar.conexao import Conexao


class Pessoa:
# classe abstrata para ser herdada por clientes e fornecedores
   
    def __init__(self, nome=None, pessoa=None, cnpj_cpf=None, rg_ie=None, tel=None,email=None,ender=None,
                bairro=None, cidade=None, uf=None, ativo=None, data_cad=None):
        
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
        self.data_cad = data_cad

    def incluir(self,tabela):
        conn = Conexao() # conecta ao banco de dados   
        conn.cursor.execute(""" INSERT INTO clientes (nome, pessoa, cnpj_cpf,rg_ie,telefone,email,
            endereco,bairro,cidade,uf,ativo) VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
            (self.nome,self.pessoa,self.cnpj_cpf,self.rg_ie,self.tel,self.email,self.ender,self.bairro,
             self.cidade,self.uf,self.ativo))
        conn.conex.commit() # envia as inserções para o banco
        conn.desconecta_bd()

        print("Registro adicionado com sucesso!")
        