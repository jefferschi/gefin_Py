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
            pass
        else:
            print('arquivo de dados não exite')