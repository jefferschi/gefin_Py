import ttkbootstrap as tb
from ttkbootstrap.constants import *

from tkinter import *

from utilitar.conexao import ICONE_DF
from models.clientes import Cliente



"""
colocar o que seriam as views no Django, ver se precisará criar módulos.
criar arquivos separados para a interface gráfica, como cliente_interface.py, fornecedor_interface.py,
etc., onde cada arquivo contém a definição da interface gráfica para o respectivo recurso.
"""

### alterações:
# todos os campos estão como não editáveis ao abrir, exceto os dados principais que podem servir como busca
# ao clicar em incluir, a tela fica aberta para edição, exceto codigo, e o botão incluir passa a se chamar salvar


class ClienteTelaCad:
    def __init__(self):
        self.janela = tb.Toplevel()
        self.janela.resizable(0,0)
        self.tela("Cadastro de Clientes", "600x450+70+70")
    
    def tela(self, titulo, geo):
        # deixar todos os campos não editáveis ao abrir, exceto código
        self.janela.title(titulo)
        self.janela.geometry(geo)
        self.janela.iconbitmap(ICONE_DF)
        
        # quadro para informações básicas do cliente
        self.qd_dados = tb.Labelframe(self.janela, text='Dados do Cliente', bootstyle=INFO)
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

        # colocar verificação de campos obrigatorios vazios antes de instanciar o objeto
        # colocar verificação cnpj único (no banco de dados já é único)


        cliente = Cliente(nome=nome,pessoa=pessoa, cnpj_cpf=cnpj,rg_ie=rg,tel=tel,email=email,ender=ender,bairro=bairro,
                          cidade=cidade,uf=uf,ativo=ativo)
        
        print(cliente.nome)
        print(nome)

        
        #cliente.incluir("clientes")
        cliente.info_teste("clientes")

        self.volta_tl_cad()


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

"""        
   # anotações sobre os botoes a incluir     
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
        self.janela = tb.Toplevel()
        self.janela.resizable(0,0)
        self.tela("Lista de Clientes", "600x450+100+70")
    
    def tela(self, titulo, geo):
        # deixar todos os campos não editáveis ao abrir, exceto código
        self.janela.title(titulo)
        self.janela.geometry(geo)
        self.janela.iconbitmap(ICONE_DF)
