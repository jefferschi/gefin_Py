import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs.dialogs import Messagebox as msg

from tkinter import *

from controle.conexao import ICONE_DF

class BaseTelaCad:
    def __init__(self,tabela,geo):
        self.janela = tb.Toplevel()
        self.janela.resizable(0,0)
        self.janela.title(f'Cadastro de {tabela}')
        self.janela.geometry(geo)
        self.janela.iconbitmap(ICONE_DF)
        self.tela(tabela=tabela)
    

    def tela(self,tabela):        
        # quadro para informações básicas do cliente/fornecedor
        self.qd_dados = tb.Labelframe(self.janela, text=f'Dados do {tabela}', bootstyle=INFO)
        self.qd_dados.grid(row=0,column=0, padx=10, pady=5, ipadx=5, ipady=5, sticky=W)
        
        self.rt_cod = tb.Label(self.qd_dados, text='Código')
        self.rt_cod.grid(row=0, column=0, sticky=W, padx=5, pady=2)
        self.ent_codigo = tb.Entry(self.qd_dados, width=15)
        self.ent_codigo.grid(row=1, column=0, sticky=W, padx=5)
        self.ent_codigo.focus()
        
        self.rt_nome = tb.Label(self.qd_dados, text='Nome')
        self.rt_nome.grid(row=0, column=1, sticky=W, padx=5, pady=2)
        self.ent_nome = tb.Entry(self.qd_dados, width=50)
        self.ent_nome.grid(row=1, column=1, sticky=W, padx=5, columnspan=2)
        
        self.v_ativo = IntVar(self.qd_dados, value=1) #variável para o check button campo Ativo 
        self.cbt_ativo = tb.Checkbutton(self.qd_dados, text='Ativo', variable=self.v_ativo,
                                    onvalue=1, offvalue=0)
        self.cbt_ativo.grid(row=0, column=2, padx=5, sticky=E)

        self.dic_pessoa = {'F':'Física','J':'Jurídica'} # para usar ao salvar no banco de dados
        self.rt_pessoa = tb.Label(self.qd_dados, text='Pessoa')
        self.rt_pessoa.grid(row=2, column=0, sticky=W, padx=5, pady=2)
        self.cbx_pessoa = tb.Combobox(self.qd_dados, values=['Física','Jurídica'], width=13)
        self.cbx_pessoa.grid(row=3, column=0, sticky=W, padx=5)
        
        self.rt_cpf_cnpj = tb.Label(self.qd_dados, text='CPF/CNPJ')
        self.rt_cpf_cnpj.grid(row=2, column=1, sticky=W, padx=5, pady=2)
        self.ent_cpf_cnpj = tb.Entry(self.qd_dados, width=30)
        self.ent_cpf_cnpj.grid(row=3, column=1, sticky=W, padx=5)

        self.rt_rg_ie = tb.Label(self.qd_dados, text='RG/IE')
        self.rt_rg_ie.grid(row=2, column=2, sticky=W, padx=5, pady=2)
        self.ent_rg_ie = tb.Entry(self.qd_dados, width=15, state=READONLY)
        self.ent_rg_ie.grid(row=3, column=2, sticky=W, padx=5)

        # quadro 2 para informações de endereço e contato
        self.qd_compl = tb.Labelframe(self.janela, text='Complementos', bootstyle=INFO)
        self.qd_compl.grid(row=1,column=0, padx=10, pady=5, ipadx=5, ipady=5, sticky=W)
        
        self.rt_tel = tb.Label(self.qd_compl, text='Telefone')
        self.rt_tel.grid(row=0,column=0, sticky=W, padx=5, pady=2)
        self.ent_tel = tb.Entry(self.qd_compl,width=15, state=READONLY)
        self.ent_tel.grid(row=1, column=0, sticky=W, padx=5)

        self.rt_email = tb.Label(self.qd_compl, text='E-mail')
        self.rt_email.grid(row=0,column=1, sticky=W, padx=5, pady=2)
        self.ent_email = tb.Entry(self.qd_compl,width=39, state=READONLY)
        self.ent_email.grid(row=1, column=1, sticky=W, padx=5, columnspan=2)

        self.rt_end = tb.Label(self.qd_compl, text='Endereço')
        self.rt_end.grid(row=2,column=0, sticky=W, padx=5, pady=2)
        self.ent_end = tb.Entry(self.qd_compl,width=69, state=READONLY)
        self.ent_end.grid(row=3, column=0, sticky=W, padx=5, columnspan=3)

        self.rt_bairro = tb.Label(self.qd_compl, text='Bairro')
        self.rt_bairro.grid(row=4, column=0, sticky=W, padx=5, pady=2)
        self.ent_bairro = tb.Entry(self.qd_compl, width=25, state=READONLY)
        self.ent_bairro.grid(row=5, column=0, sticky=W, padx=5)

        self.rt_cidade = tb.Label(self.qd_compl, text='Cidade')
        self.rt_cidade.grid(row=4, column=1, sticky=W, padx=5, pady=2)
        self.ent_cidade = tb.Entry(self.qd_compl, width=25, state=READONLY)
        self.ent_cidade.grid(row=5, column=1, sticky=W, padx=5)
        
        self.rt_uf = tb.Label(self.qd_compl, text='UF')
        self.rt_uf.grid(row=4, column=2, sticky=W, padx=5, pady=2)
        self.ent_uf = tb.Entry(self.qd_compl, width=4, state=READONLY)
        self.ent_uf.grid(row=5, column=2, sticky=W, padx=5)

        self.rt_data_cad = tb.Label(self.qd_compl, text='Data do cadastro')
        self.rt_data_cad.grid(row=6, column=0, sticky=W, padx=5, pady=2)
        self.ent_data_cad = tb.Entry(self.qd_compl, width=10, state=READONLY)
        self.ent_data_cad.grid(row=7, column=0, sticky=W, padx=5)
        
        # quadro para os botões
        self.qd_bt = tb.Frame(self.janela)
        self.qd_bt.grid(row=2,column=0,sticky=W, padx=5, pady=10)

        self.bt_novo = tb.Button(self.qd_bt, text='Novo', bootstyle=SUCCESS, command=self.libera_edicao)
        self.bt_novo.pack(side=LEFT, padx=(5,0))

        self.bt_busca = tb.Button(self.qd_bt, text='Buscar', bootstyle=INFO)
        self.bt_busca.pack(side=LEFT, padx=(5,0))

        self.bt_altera = tb.Button(self.qd_bt, text='Alterar', bootstyle=SECONDARY)
        self.bt_altera.pack(side=LEFT, padx=(5,0))

        self.bt_limpa = tb.Button(self.qd_bt, text='Limpar', bootstyle=WARNING, command=self.limpa_dados)
        self.bt_limpa.pack(side=LEFT, padx=(5,0))
        

    def libera_edicao(self):
        self.ent_codigo.config(state=READONLY)
        self.ent_rg_ie.configure(state=ACTIVE)
        self.ent_tel.configure(state=ACTIVE)
        self.ent_email.configure(state=ACTIVE)
        self.ent_end.configure(state=ACTIVE)
        self.ent_bairro.configure(state=ACTIVE)
        self.ent_cidade.configure(state=ACTIVE)
        self.ent_uf.configure(state=ACTIVE)

        #substitui os botões na tela
        self.qd_bt.destroy()
        
        self.qd_bt = tb.Frame(self.janela)
        self.qd_bt.grid(row=2,column=0,sticky=W, padx=5, pady=10)

        self.bt_salva = tb.Button(self.qd_bt, text='Salvar', bootstyle=SUCCESS, command=self.pega_dados)
        self.bt_salva.pack(side=LEFT, padx=(5,0))
        
        self.bt_limpa = tb.Button(self.qd_bt, text='Limpar', bootstyle=WARNING, command=self.limpa_dados)
        self.bt_limpa.pack(side=LEFT, padx=(5,0))

        self.bt_cancela = tb.Button(self.qd_bt, text='Cancelar', bootstyle=DANGER, command=self.volta_tl_cad)
        self.bt_cancela.pack(side=LEFT, padx=(5,0))

    def volta_tl_cad(self):
        self.limpa_dados()
        self.bloqueia_edicao()

    def bloqueia_edicao(self):
        self.ent_codigo.config(state=ACTIVE)
        self.ent_rg_ie.configure(state=READONLY)
        self.ent_tel.configure(state=READONLY)
        self.ent_email.configure(state=READONLY)
        self.ent_end.configure(state=READONLY)
        self.ent_bairro.configure(state=READONLY)
        self.ent_cidade.configure(state=READONLY)
        self.ent_uf.configure(state=READONLY)
        
        #substitui os botões na tela
        self.qd_bt.destroy()
        
        self.qd_bt = tb.Frame(self.janela)
        self.qd_bt.grid(row=2,column=0,sticky=W, padx=5, pady=10)

        self.bt_novo = tb.Button(self.qd_bt, text='Novo', bootstyle=SUCCESS, command=self.libera_edicao)
        self.bt_novo.pack(side=LEFT, padx=(5,0))

        self.bt_busca = tb.Button(self.qd_bt, text='Buscar', bootstyle=INFO)
        self.bt_busca.pack(side=LEFT, padx=(5,0))

        self.bt_altera = tb.Button(self.qd_bt, text='Alterar', bootstyle=SECONDARY)
        self.bt_altera.pack(side=LEFT, padx=(5,0))

        self.bt_limpa = tb.Button(self.qd_bt, text='Limpar', bootstyle=WARNING, command=self.limpa_dados)
        self.bt_limpa.pack(side=LEFT, padx=(5,0))
        


    def pega_dados(self):        

        nome = self.ent_nome.get()
        pessoa = self.cbx_pessoa.get()
        cnpj = self.ent_cpf_cnpj.get()
        rg = self.ent_rg_ie.get()
        tel = self.ent_tel.get()
        email = self.ent_email.get()
        ender = self.ent_end.get()
        bairro = self.ent_bairro.get()
        cidade = self.ent_cidade.get()
        uf = self.ent_uf.get()
        ativo = self.v_ativo.get()

        """
        # verificação de campos obrigatorios vazios antes de instanciar o objeto
        if nome == "":
            msg.show_info('Preencha o nome do cliente',title='Alerta', parent=self.janela, alert=False)
        else:

            cliente = Cliente(nome=nome,pessoa=pessoa, cnpj_cpf=cnpj,rg_ie=rg,tel=tel,email=email,ender=ender,bairro=bairro,
                            cidade=cidade,uf=uf,ativo=ativo)
            
            cliente.incluir("clientes")
            msg.ok('Registro adicionado com sucesso', title='Informação', parent=self.janela, alert=False)
            
            self.volta_tl_cad()
        """

    def limpa_dados(self):
        self.ent_codigo.delete(0, END)
        self.ent_nome.delete(0, END)
        self.cbx_pessoa.delete(0, END)
        self.ent_cpf_cnpj.delete(0, END)
        self.ent_rg_ie.delete(0, END)
        self.ent_tel.delete(0, END)
        self.ent_email.delete(0, END)
        self.ent_end.delete(0, END)
        self.ent_bairro.delete(0, END)
        self.ent_cidade.delete(0, END)
        self.ent_uf.delete(0, END)


# a ideia é tentar fazer como em models. verificar sobre a notação @abstractmethod se preciso mesmo usar
# ou se posso fazer como em models, aparentemente funciona e é mais simples. Creio que com notação é obrigado
# a usar o método

# tentar usar com o fornecedor primeiro.

"""class BaseTela(ABC):
    def __init__(self, root):
        self.root = root

    @abstractmethod
    def criar_interface(self):
        pass

class TelaCliente(BaseTela):
    def criar_interface(self):
        # Crie a interface comum para a tela de cliente aqui
        # Adicione campos e widgets específicos para clientes

class TelaFornecedor(BaseTela):
    def criar_interface(self):
        # Crie a interface comum para a tela de fornecedor aqui
        # Adicione campos e widgets específicos para fornecedores
        # Adicione campos adicionais específicos para fornecedores"""