import ttkbootstrap as tb
from ttkbootstrap.constants import *


class Programa:

    def __init__(self):
        self.raiz = tb.Window(themename='flatly')
        self.janela()
        self.menu_raiz()
        self.raiz.mainloop()
    
    def janela(self):        
        self.raiz.title("Gestão Financeira - Versão Desenvolvimento")
        self.raiz.geometry("800x500+50+50")
        self.raiz.iconbitmap('img\icone.ico')

    def menu_raiz(self):
        self.barra_menu = tb.Menu(self.raiz)
        self.raiz.config(menu=self.barra_menu) # atribui a barra menu à janela principal

        # menus de cadastro
        self.menu_cad = tb.Menu(self.barra_menu, tearoff=0)
        self.barra_menu.add_cascade(label='Cadastro', menu=self.menu_cad, underline=0)

        self.menu_cad.add_command(label='Cliente', command=None)
        self.menu_cad.add_command(label='Fornecedor', command=None)
        self.menu_cad.add_separator()
        self.menu_cad.add_command(label='Forma Pagto', command=None)
        self.menu_cad.add_command(label='Tipo de despesa', command=None)
        self.menu_cad.add_command(label='Despesa', command=None)
        self.menu_cad.add_separator()
        self.menu_cad.add_command(label='Sair', command=self.raiz.quit)



if __name__ == "__main__":
    Programa()
