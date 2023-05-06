""" arquivo para criar e fazer manutenção na tabela de dados"""

import sqlite3
import os

class TabelaDados:
    
    def conecta_bd(self):
            """conecta no banco de dados"""
            self.conn = sqlite3.connect('gefin.db')
            self.cursor = self.conn.cursor() #habilita escrever em sql
        
    def desconecta_bd(self):
        """desconecta do banco de dados"""
        self.conn.close()

    def cria_tabelas(self):
        # confere se o arquivo existe
        arquivo = 'gefin.db'
        if(os.path.exists(arquivo)):
            print('tabela já existe')
        else:
            self.conecta_bd()

            # cria tabela clientes
            self.cursor.execute(''' 
                CREATE TABLE IF NOT EXISTS clientes (
                    codigo INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    nome VARCHAR(100) NOT NULL,
                    cpf CHAR(11) UNIQUE,
                    rg VARCHAR(15),
                    nascimento DATE,
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