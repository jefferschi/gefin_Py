from controle.conexao import Conexao

class Categoria:

    def __init__(self,categoria):
        self.categoria = categoria
        
    def incluir(self, tabela): # colocar a tabela que será armazenada os dados como parâmetro

        #self.data_cad = datetime.today().strftime('%Y-%m-%d')

        sql = (f'INSERT INTO {tabela} (categoria) VALUES (?)')

        conn = Conexao() # conecta ao banco de dados

        conn.cursor.execute(sql,(self.categoria,)) # quando for apenas um parâmetro, deve-se colocar uma vírgula
        conn.conex.commit() # envia as inserções para o banco
        conn.desconecta_bd()