#import ttkbootstrap as tb
#from ttkbootstrap.constants import *

from controle.conexao import Conexao
from datetime import *


class Pessoa:
# classe abstrata para ser herdada por clientes e fornecedores
   
   # se colocar o none na frente do parâmetro, não será obrigatório o seu uso ao herdá-lo
    def __init__(self, nome, pessoa, cnpj_cpf, rg_ie, tel,email,ender,
                bairro, cidade, uf, ativo, data_cad):
        
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

    # INCLUIR fazer checagem de cnpj único
    def incluir(self, tabela): # colocar a tabela que será armazenada os dados como parâmetro

        #self.data_cad = datetime.today().strftime('%Y-%m-%d')

        sql = (f'INSERT INTO {tabela} (nome, pessoa, cnpj_cpf,rg_ie,telefone,email,endereco,bairro,'
        'cidade,uf,ativo,data_cad) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)')

        conn = Conexao() # conecta ao banco de dados

        conn.cursor.execute(sql,(self.nome,self.pessoa,self.cnpj_cpf,self.rg_ie,self.tel,self.email,self.ender,self.bairro,
             self.cidade,self.uf,self.ativo,self.data_cad))
        conn.conex.commit() # envia as inserções para o banco
        conn.desconecta_bd()

    def alterar(self, tabela):
        pass
    
    def info_teste(self, tabela):
        print(self.nome,tabela)
        