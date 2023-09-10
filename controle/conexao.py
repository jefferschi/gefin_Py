import sqlite3

ICONE_DF = 'img\icone.ico'

class Conexao:
    
    # método construtor se conecta e habilita o cursor
    def __init__(self):
        banco_dados = ('utilitar\gefin.db')
        self.conex = sqlite3.connect(banco_dados) # conecta ao banco de dados
        self.cursor = self.conex.cursor() #habilita escrever em sql        

    def desconecta_bd(self):
        self.conex.close() #desconecta do banco de dados