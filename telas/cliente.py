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
        self.janela.geometry("600x450+55+55")
        self.janela.iconbitmap('img\icone.ico')
        self.janela.resizable(False,False)
        self.tela()
    
    def tela(self):

        # deixar todos os campos não editáveis ao abrir, exceto código

        # quadro para informações básicas do cliente
        self.quadro = tb.Labelframe(self.janela, text='Dados do Cliente', bootstyle=INFO)
        self.quadro.grid(row=0,column=0, padx=10, pady=5, ipadx=5, ipady=5, sticky=W)
        
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

        # quadro 2 para informações de endereço e contato
        self.quadro2 = tb.Labelframe(self.janela, text='Complementos', bootstyle=INFO)
        self.quadro2.grid(row=1,column=0, padx=10, pady=5, ipadx=5, ipady=5, sticky=W)

        # quadro para separar algumas informações dentro do quadro 2
        self.q_contat = tb.Frame(self.quadro2)
        self.q_contat.grid(row=0,column=0,sticky=W, padx=5, pady=2)
        
        tb.Label(self.q_contat, text='Telefone').grid(row=0,column=0, sticky=W, padx=5, pady=2)
        self.tel = tb.Entry(self.q_contat,width=15)
        self.tel.grid(row=1, column=0, sticky=W, padx=5)

        tb.Label(self.q_contat, text='E-mail').grid(row=0,column=1, sticky=W, padx=5, pady=2)
        self.email = tb.Entry(self.q_contat,width=50)
        self.email.grid(row=1, column=1, sticky=W, padx=5)
        
        tb.Label(self.quadro2, text='Endereço').grid(row=1,column=0, sticky=W, padx=10, pady=2)
        self.endereco = tb.Entry(self.quadro2,width=68)
        self.endereco.grid(row=2, column=0, sticky=W, padx=10)

        # quadro para complemento de endereço para separar informações dentro do quadro 2
        self.qd_end_compl = tb.Frame(self.quadro2)
        self.qd_end_compl.grid(row=3,column=0,sticky=W, padx=5, pady=2)

        tb.Label(self.qd_end_compl, text='Bairro').grid(row=0, column=0, sticky=W, padx=5, pady=2)
        self.bairro = tb.Entry(self.qd_end_compl, width=25)
        self.bairro.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        tb.Label(self.qd_end_compl, text='Cidade').grid(row=0, column=1, sticky=W, padx=5, pady=2)
        self.cidade = tb.Entry(self.qd_end_compl, width=25)
        self.cidade.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        tb.Label(self.qd_end_compl, text='UF').grid(row=0, column=2, sticky=W, padx=5, pady=2)
        self.uf = tb.Entry(self.qd_end_compl, width=4)
        self.uf.grid(row=1, column=2, sticky=W, padx=5, pady=2)

        # quadro para os botões
        self.qd_bt = tb.Frame(self.janela)
        self.qd_bt.grid(row=4,column=0,sticky=W, padx=5, pady=10)

        self.bt_inclui = tb.Button(self.qd_bt, text='Inclui', bootstyle=SUCCESS)
        self.bt_inclui.pack(side=LEFT, padx=(5,0))

        self.bt_altera = tb.Button(self.qd_bt, text='Altera', bootstyle=INFO)
        self.bt_altera.pack(side=LEFT, padx=(5,0))

        self.bt_busca = tb.Button(self.qd_bt, text='Busca', bootstyle=WARNING)
        self.bt_busca.pack(side=LEFT, padx=(5,0))

    
        
"""        
        
        botoes:
        inclui (abre os campos para inclusão, exceto código que estava aberto e será não editável)
        altera (abre os campos para edição, exceto código que estava aberto e será não editável)
        busca:  (se houver)
            busca
            cancela
            seleciona
        salvar (disponibilizado quando quando o botão inclui ou altera for acionado)

"""

class ClienteTelaLista:
    def __init__(self):
        pass