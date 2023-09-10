import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs.dialogs import Messagebox as msg

from tkinter import *

from datetime import *

from controle.conexao import ICONE_DF
from models.clientes import Cliente


class ClienteTelaLista:
    def __init__(self):
        self.janela = tb.Toplevel()
        self.janela.resizable(0,0)
        self.tela("Lista de Clientes", "600x450+100+70")        
    
    def tela(self, titulo, geo):        
        self.janela.title(titulo)
        self.janela.geometry(geo)
        self.janela.iconbitmap(ICONE_DF)
    

        # quadro para os campos de busca



        # quadro para os botões
        self.qd_bt = tb.Frame(self.janela)
        self.qd_bt.grid(row=0,column=0,sticky=W, padx=5, pady=10)

        self.bt_busca = tb.Button(self.qd_bt, text='Buscar', bootstyle=INFO, command=None)
        self.bt_busca.pack(side=LEFT, padx=(5,0))

        self.bt_limpa = tb.Button(self.qd_bt, text='Limpar', bootstyle=WARNING,command=None)
        self.bt_limpa.pack(side=LEFT, padx=(5,0))

        self.bt_seleciona = tb.Button(self.qd_bt, text='Selecionar', bootstyle=SECONDARY, command=None)
        self.bt_seleciona.configure(state='disabled')
        self.bt_seleciona.pack(side=LEFT, padx=(5,0))
        

  

        # quadro para a treeview

        
   
    # fazer alternância

