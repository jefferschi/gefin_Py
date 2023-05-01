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

        # menus de cadastros
        self.menu_cad = tb.Menu(self.barra_menu, tearoff=0)
        self.barra_menu.add_cascade(label='Cadastro', menu=self.menu_cad, underline=0)

        self.menu_cad.add_command(label='Cliente', command=None, underline=0)
        self.menu_cad.add_command(label='Fornecedor', command=None, underline=0)
        self.menu_cad.add_separator()
        self.menu_cad.add_command(label='Forma Pagto', command=None, underline=6)
        self.menu_cad.add_command(label='Tipo de despesa', command=None, underline=0)
        self.menu_cad.add_command(label='Despesa', command=None, underline=0)
                

        # menus de movimento
        self.menu_mov = tb.Menu(self.barra_menu, tearoff=0)
        self.barra_menu.add_cascade(label='Movimento', menu=self.menu_mov, underline=0)

        self.menu_mov.add_command(label='Contas a Pagar', command=None, underline=9)
        self.menu_mov.add_command(label='Contas a Receber', command=None, underline=9)
        self.menu_mov.add_separator()
        self.menu_mov.add_command(label='Fluxo de Caixa', command=None, underline=9)


        # menus de relatorios
        self.menu_rel = tb.Menu(self.barra_menu, tearoff=0)
        self.barra_menu.add_cascade(label='Relatórios', menu=self.menu_rel, underline=0)

        self.menu_rel.add_command(label='Comparativo Gráfico', command=None, underline=12)
        self.menu_rel.add_separator()
        self.menu_rel.add_command(label='Contas a Pagar', command=None, underline=9)
        self.menu_rel.add_command(label='Contas a Receber', command=None, underline=9)
        self.menu_rel.add_command(label='Fluxo de Caixa', command=None, underline=9)


        # menus de utilitários
        self.menu_util = tb.Menu(self.barra_menu, tearoff=0)
        self.barra_menu.add_cascade(label='Utilitários', menu=self.menu_util, underline=0)

        self.menu_util.add_command(label='Atualizar', command=None, underline=0)
        self.menu_util.add_command(label='Versão e Licença', command=None, underline=0)
        self.menu_util.add_separator()
        self.menu_util.add_command(label='Sair', command=self.raiz.quit, underline=3)


if __name__ == "__main__":
    Programa()