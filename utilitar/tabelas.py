""" arquivo para criar e fazer manutenção na tabela de dados"""

import sqlite3
import os

ICONE_DF = 'img\icone.ico'

class TabelaDados:
    
    def __init__(self):
        self.conex = sqlite3.connect('dbgefin.db')
        self.cursor = self.conex.cursor()

    '''
    def conecta_bd(self):
            """conecta no banco de dados"""
            self.conn = sqlite3.connect('dbgefin.db')
            self.cursor = self.conn.cursor() #habilita escrever em sql
    '''
    def desconecta_bd(self):
        """desconecta do banco de dados"""
        self.conex.close()

    def cria_tabelas(self):
        """
        []CRIAR BARRA DE PROGRESSO

        """
        # confere se o arquivo existe
        arquivo = 'gefin.db'
        if(os.path.exists(arquivo)):
            print('tabela já existe')
        else:
            self.conex  # cria tabela clientes
            self.cursor.execute(''' 
                CREATE TABLE IF NOT EXISTS clientes (
                    codigo INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    nome VARCHAR(100) NOT NULL,
                    pessoa CHAR(1),
                    cnpj_cpf VARCHAR(14) UNIQUE,
                    rg_ie VARCHAR(15),
                    telefone TEXT,
                    email TEXT,
                    endereco TEXT,
                    bairro TEXT,
                    cidade TEXT,
                    uf CHAR(2),
                    ativo INTEGER
                );
            ''')
            print('tabela CLIENTES criada!')

        self.desconecta_bd()