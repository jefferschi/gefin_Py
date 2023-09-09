import sqlite3

ICONE_DF = 'img\icone.ico'

class Conexao:
    
    def __init__(self):
        self.conex = sqlite3.connect('gefin.db') # conecta ao banco de dados
        self.cursor = self.conex.cursor() #habilita escrever em sql        

    def desconecta_bd(self):
        self.conex.close() #desconecta do banco de dados