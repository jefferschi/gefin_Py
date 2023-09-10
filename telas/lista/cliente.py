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
    

