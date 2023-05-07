"""
Em vez de chamar o método grid() para cada widget, você pode agrupar as chamadas em uma única chamada 
ao final da função tela(). Isso reduz a quantidade de atualizações de layout necessárias e melhora o 
desempenho.

Em vez de usar a função pack() para os botões, você pode utilizar o método grid() para posicioná-los no 
quadro de botões. Isso ajuda a manter a consistência e torna mais fácil adicionar mais botões no futuro, 
se necessário.

Defina o estilo do tema (bootstyle) e outras configurações no início da função tela() e utilize os valores 
diretamente na criação dos widgets. Dessa forma, você evita a criação de objetos LabelStyle e ButtonStyle 
desnecessários.
"""

class ClienteTelaCad:
    def __init__(self):
        self.janela = tb.Toplevel()
        self.janela.title("Cadastro de Clientes")
        self.janela.geometry("600x450+70+70")
        self.janela.iconbitmap('img\icone.ico')
        self.janela.resizable(False, False)
        self.tela()

    def tela(self):
        # Estilos
        info_style = "info.TLabelframe"
        success_style = "success.TButton"
        info_button_style = "info.TButton"
        warning_button_style = "warning.TButton"

        # Quadro para informações básicas do cliente
        self.qd_dados = tb.Labelframe(self.janela, text='Dados do Cliente', style=info_style)
        self.qd_dados.grid(row=0, column=0, padx=10, pady=5, ipadx=5, ipady=5, sticky=W)

        self.rt_cod = tb.Label(self.qd_dados, text='Código')
        self.rt_cod.grid(row=0, column=0, sticky=W, padx=5, pady=2)
        self.ent_codigo = tb.Entry(self.qd_dados, width=15)
        self.ent_codigo.grid(row=1, column=0, sticky=W, padx=5)
        self.ent_codigo.focus()

        self.rt_nome = tb.Label(self.qd_dados, text='Nome')
        self.rt_nome.grid(row=0, column=1, sticky=W, padx=5, pady=2)
        self.ent_nome = tb.Entry(self.qd_dados, width=50)
        self.ent_nome.grid(row=1, column=1, sticky=W, padx=5, columnspan=2)

        self.v_ativo = tb.IntVar(self.qd_dados, value=1)  # variável para o check button campo Ativo
        self.cbt_ativo = tb.Checkbutton(self.qd_dados, text='Ativo', variable=self.v_ativo, onvalue=1, offvalue=0)
        self.cbt_ativo.grid(row=0, column=2, padx=5, sticky=E)

        self.dic_pessoa = {'F': 'Física', 'J': 'Jurídica'}  # para usar ao salvar no banco de dados
        self.rt_pessoa = tb.Label(self.qd_dados, text='Pessoa')
        self.rt_pessoa.grid(row=2, column=0, sticky=W, padx=5, pady=2)
        