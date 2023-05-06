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
        self.raiz = tb.Toplevel()        
        self.raiz.title("Cadastro de Clientes")
        self.raiz.geometry("800x500+55+55")
        self.raiz.iconbitmap('img\icone.ico')
        
        self.tela()       
        self.raiz.mainloop()
    
    def tela(self):
        self.quadro = tb.Labelframe(self.raiz, text='Dados do Cliente', bootstyle=SUCCESS,
                                    width=500, height=300)
        self.quadro.place(relx=0.01, rely=0.01)



class ClienteTelaLista:
    def __init__(self):
        pass