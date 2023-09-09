import ttkbootstrap as tb
from ttkbootstrap.constants import *

from utilitar.conexao import Conexao
from models.pessoas import Pessoa


class Cliente(Pessoa):
   
    def __init__(self, nome, pessoa, cnpj_cpf, rg_ie, tel,email,ender,
                bairro, cidade, uf, ativo):
        super().__init__(nome, pessoa, cnpj_cpf, rg_ie, tel,email,ender,
                bairro, cidade, uf, ativo)

    # verificar se haverá necessidade de sobrepor métodos herdados da classe abstrata.


        """ fazia parte do código cliente antes de incluir classe abstrata
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

    def incluir(self, tabela):
        sql = (f'INSERT INTO {tabela} (nome, pessoa, cnpj_cpf,rg_ie,telefone,email,endereco,bairro,'
        'cidade,uf,ativo) VALUES (?,?,?,?,?,?,?,?,?,?,?)')

        conn = Conexao() # conecta ao banco de dados

        conn.cursor.execute(sql,(self.nome,self.pessoa,self.cnpj_cpf,self.rg_ie,self.tel,self.email,self.ender,self.bairro,
             self.cidade,self.uf,self.ativo))
        conn.conex.commit() # envia as inserções para o banco
        conn.desconecta_bd()

        print("Registro adicionado com sucesso!")
    """