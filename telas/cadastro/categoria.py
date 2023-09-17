import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs.dialogs import Messagebox as msg

from tkinter import *

from datetime import *

from controle.conexao import ICONE_DF
from models.categorias import Categoria


class CategoriaTelaCad:
    def __init__(self):
        self.janela = tb.Toplevel()
        self.janela.resizable(0,0)
        self.tela("Cadastro de Categorias", "600x450+70+70")
    
    def tela(self, titulo, geo):
        self.janela.title(titulo)
        self.janela.geometry(geo)
        self.janela.iconbitmap(ICONE_DF)

     # quadro para informações
        self.qd_dados = tb.Labelframe(self.janela, text='Nome da Categoria', bootstyle=INFO)
        self.qd_dados.grid(row=0,column=0, padx=10, pady=5, ipadx=5, ipady=5, sticky=W)

        self.rt_cod = tb.Label(self.qd_dados, text='Código')
        self.rt_cod.grid(row=0, column=0, sticky=W, padx=5, pady=2)
        self.ent_codigo = tb.Entry(self.qd_dados, width=15)
        self.ent_codigo.grid(row=1, column=0, sticky=W, padx=5)
        self.ent_codigo.focus()
        
        self.rt_nome = tb.Label(self.qd_dados, text='Categoria')
        self.rt_nome.grid(row=0, column=1, sticky=W, padx=5, pady=2)
        self.ent_nome = tb.Entry(self.qd_dados, width=50)
        self.ent_nome.grid(row=1, column=1, sticky=W, padx=5, columnspan=2)
    
    # alterar botões para este contexto 
    """
    def botoes_inicio(self):
        # quadro para os botões
        self.qd_bt = tb.Frame(self.janela)
        self.qd_bt.grid(row=2,column=0,sticky=W, padx=5, pady=10)

        self.bt_novo = tb.Button(self.qd_bt, text='Novo', bootstyle=SUCCESS, command=self.libera_edicao)
        self.bt_novo.pack(side=LEFT, padx=(5,0))

        self.bt_busca = tb.Button(self.qd_bt, text='Buscar', bootstyle=INFO,command=self.busca_cliente)
        self.bt_busca.pack(side=LEFT, padx=(5,0))

        self.bt_altera = tb.Button(self.qd_bt, text='Alterar', bootstyle=SECONDARY)
        self.bt_altera.configure(state='disabled')
        self.bt_altera.pack(side=LEFT, padx=(5,0))

        self.bt_limpa = tb.Button(self.qd_bt, text='Limpar', bootstyle=WARNING, command=self.limpa_dados)
        self.bt_limpa.pack(side=LEFT, padx=(5,0))
    """