import ttkbootstrap as tb
from ttkbootstrap.constants import *


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

        self.quadro = tb.Labelframe(self.janela, text='Dados do Cliente', bootstyle=INFO,
                                    width=750, height=450)
        self.quadro.pack(side=TOP, padx=10, pady=10)
        
        tb.Label(self.quadro, text='Código').place(relx=0.01, rely=0.01)
        self.codigo = tb.Entry(self.quadro, width=15)
        self.codigo.place(relx=0.01, rely=0.055)
        self.codigo.focus()
        
        tb.Label(self.quadro, text='Nome').place(relx=0.2, rely=0.01)
        self.nome = tb.Entry(self.quadro, width=90)
        self.nome.place(relx=0.2, rely=0.055)

        tb.Label(self.quadro, text='Pessoa').place(relx=0.01, rely=0.1)
        self.pessoa = tb.Combobox(self.quadro, values=('Física','Jurídica'), width=17)
        self.pessoa.place(relx=0.01,rely=0.2)

        tb.Label(self.quadro, text='CPF').place(relx=0.2, rely=0.1)
        self.nome = tb.Entry(self.quadro, width=90)
        self.nome.place(relx=0.2, rely=0.2)

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