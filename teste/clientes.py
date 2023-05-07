import sqlite3
from tkinter import Tk, Label, Entry, Button

"""
exemplo
criar uma classe cliente e insere os dados no banco de dados por meio de um formulário
"""

class Cliente:
    def _init_(self, codigo, nome, cpf):
        self.codigo = codigo
        self.nome = nome
        self.cpf = cpf

    def inserir_no_banco(self):
        # Conexão com o banco de dados
        conexao = sqlite3.connect("banco_dados.db")
        cursor = conexao.cursor()

        # Criação da tabela (se ainda não existir)
        cursor.execute("CREATE TABLE IF NOT EXISTS clientes (codigo INTEGER, nome TEXT, cpf TEXT)")

        # Inserção do cliente na tabela
        cursor.execute("INSERT INTO clientes VALUES (?, ?, ?)", (self.codigo, self.nome, self.cpf))
        conexao.commit()

        # Fechamento da conexão
        conexao.close()

        print("Cliente adicionado com sucesso!")

class Formulario:
    def _init_(self, janela):
        self.janela = janela
        self.janela.title("Formulário de Cliente")

        # Labels e campos de entrada
        self.label_codigo = Label(janela, text="Código:")
        self.label_codigo.grid(row=0, column=0)
        self.entry_codigo = Entry(janela)
        self.entry_codigo.grid(row=0, column=1)

        self.label_nome = Label(janela, text="Nome:")
        self.label_nome.grid(row=1, column=0)
        self.entry_nome = Entry(janela)
        self.entry_nome.grid(row=1, column=1)

        self.label_cpf = Label(janela, text="CPF:")
        self.label_cpf.grid(row=2, column=0)
        self.entry_cpf = Entry(janela)
        self.entry_cpf.grid(row=2, column=1)

        # Botão de envio
        self.botao_enviar = Button(janela, text="Enviar", command=self.adicionar_cliente)
        self.botao_enviar.grid(row=3, column=0, columnspan=2)

    def adicionar_cliente(self):
        codigo = self.entry_codigo.get()
        nome = self.entry_nome.get()
        cpf = self.entry_cpf.get()

        # Instanciação do cliente
        cliente = Cliente(codigo, nome, cpf)
        cliente.inserir_no_banco()

        # Limpar os campos de entrada após a inserção
        self.entry_codigo.delete(0, "end")
        self.entry_nome.delete(0, "end")
        self.entry_cpf.delete(0, "end")

# Criação da janela Tkinter
janela = Tk()

# Instanciação do formulário
formulario = Formulario(janela)

# Execução da janela
janela.mainloop()
class Cliente:
    def _init_(self, nome=None, cpf=None, codigo=None, endereco=None, telefone=None, email=None):
        self.nome = nome
        self.cpf = cpf
        self.codigo = codigo
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

# Exemplo de uso
cliente1 = Cliente(nome="João", cpf="123.456.789-00")
cliente2 = Cliente(codigo=1, nome="Maria", cpf="987.654.321-00", endereco="Rua X", telefone="123456789", email="maria@example.com")