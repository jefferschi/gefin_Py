import ttkbootstrap as tb
from ttkbootstrap.constants import *

from tkinter import *

#from models.clientes import Cliente


"""
colocar o que seriam as views no Django, ver se precisará criar módulos.
criar arquivos separados para a interface gráfica, como cliente_interface.py, fornecedor_interface.py,
etc., onde cada arquivo contém a definição da interface gráfica para o respectivo recurso.
"""

class ClienteTelaCad:
    def __init__(self):
        self.janela = tb.Toplevel()
        self.janela.title("Cadastro de Clientes")
        self.janela.geometry("800x500+55+55")
        self.janela.iconbitmap('img\icone.ico')
        self.janela.resizable(False,False)
        self.tela()
    
    def tela(self):

        # quadro para informações básicas do cliente

        self.quadro = tb.Labelframe(self.janela, text='Dados do Cliente', bootstyle=INFO)
        self.quadro.grid(row=0,column=0, padx=10, pady=5, ipadx=5, ipady=5)
        
        tb.Label(self.quadro, text='Código').grid(row=0, column=0, sticky=W, padx=5, pady=2)
        self.codigo = tb.Entry(self.quadro, width=15)
        self.codigo.grid(row=1, column=0, sticky=W, padx=5)
        self.codigo.focus()

        tb.Label(self.quadro, text='Nome').grid(row=0, column=1, sticky=W, padx=5, pady=2)
        self.nome = tb.Entry(self.quadro, width=50)
        self.nome.grid(row=1, column=1, sticky=W, padx=5)

        ativo = IntVar(self.quadro, value=1) #variável para o check button campo Ativo 
        self.ativo = tb.Checkbutton(self.quadro, text='Ativo', variable=ativo,
                                    onvalue=1, offvalue=0)
        self.ativo.grid(row=0, column=2, padx=(0,5), sticky=E)
        
        
        tb.Label(self.quadro, text='Pessoa').grid(row=2, column=0, sticky=W, padx=5, pady=2)
        self.pessoa = tb.Combobox(self.quadro, values=['Física','Jurídica'], width=13)
        self.pessoa.grid(row=3, column=0, sticky=W, padx=5)
        
        tb.Label(self.quadro, text='CPF/CNPJ').grid(row=2, column=1, sticky=W, padx=5, pady=2)
        self.cpf_cnpj = tb.Entry(self.quadro, width=30)
        self.cpf_cnpj.grid(row=3, column=1, sticky=W, padx=5)

        tb.Label(self.quadro, text='RG/IE').grid(row=2, column=2, sticky=W, padx=5, pady=2)
        self.rg_ie = tb.Entry(self.quadro, width=15)
        self.rg_ie.grid(row=3, column=2, sticky=W, padx=5)


        

"""
        codigo 
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
"""

class ClienteTelaLista:
    def __init__(self):
        pass