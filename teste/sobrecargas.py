"""
Neste exemplo, o construtor __init__ da classe Cliente aceita um número variável de argumentos 
posicionais (*args) e argumentos nomeados opcionais (**kwargs). No bloco if-elif-else, verificamos 
o tamanho de args para determinar qual configuração de atributos está sendo usada.
Se args tiver 2 elementos, assumimos que os argumentos são nome e cpf. Se args tiver 6 elementos,
assumimos que os argumentos são codigo, nome, cpf, endereco, telefone e email. Caso contrário,
lançamos um erro de valor inválido.
Em seguida, percorremos os argumentos nomeados opcionais em kwargs e usamos a função setattr para 
atribuir dinamicamente esses atributos ao objeto Cliente.
"""

class Cliente:
    def __init__(self, *args, **kwargs):
        if len(args) == 2:
            self.nome = args[0]
            self.cpf = args[1]
        elif len(args) == 6:
            self.codigo = args[0]
            self.nome = args[1]
            self.cpf = args[2]
            self.endereco = args[3]
            self.telefone = args[4]
            self.email = args[5]
        else:
            raise ValueError("Número inválido de argumentos")

        for key, value in kwargs.items():
            setattr(self, key, value)

##########################

class Cliente:
    def __init__(self, *args):
        self.atributos = {
            'codigo': None,
            'nome': None,
            'cpf': None,
            'endereco': None,
            'telefone': None,
            'email': None
        }

        if len(args) > len(self.atributos):
            raise ValueError("Número inválido de argumentos")

        for i, arg in enumerate(args):
            atributo = list(self.atributos.keys())[i]
            self.atributos[atributo] = arg

        # Exemplo: atribuição direta dos atributos individuais
        # self.codigo = self.atributos['codigo']
        # self.nome = self.atributos['nome']
        # self.cpf = self.atributos['cpf']
        # ...

        # Ou, se preferir, você pode acessar os atributos diretamente pelo dicionário:
        # Exemplo: self.atributos['codigo'], self.atributos['nome'], self.atributos['cpf'], ...
        
######################################



"""
Essas abordagens permitem criar diferentes formas de inicializar a classe Cliente e fornecer 
flexibilidade ao usuário, sem a necessidade de usar a verificação direta de *args ou len(args) 
para determinar o número de argumentos. No entanto, vale ressaltar que a melhor abordagem dependerá 
dos requisitos específicos do seu programa."""
#########

"""
Neste exemplo, definimos um único construtor __init__ com argumentos opcionais que possuem valores 
padrão definidos como None. Assim, você pode criar objetos Cliente fornecendo apenas os argumentos 
desejados e o restante assumirá o valor padrão.
"""

class Cliente:
    def __init__(self, nome=None, cpf=None, codigo=None, endereco=None, telefone=None, email=None):
        self.nome = nome
        self.cpf = cpf
        self.codigo = codigo
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

###############################
"""
Exemplo: Sobrecarga usando verificações de tipo
Neste exemplo, temos um construtor padrão __init__ que recebe apenas nome e cpf. Além disso, 
adicionamos um método de classe from_dados_completos que permite criar um objeto Cliente com todos os
 atributos. A verificação de tipo é feita dentro desse método, garantindo que o argumento codigo seja 
 um valor inteiro.

"""

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    @classmethod
    def from_dados_completos(cls, codigo, nome, cpf, endereco, telefone, email):
        if not isinstance(codigo, int):
            raise TypeError("O código deve ser um valor inteiro")
        cliente = cls(nome, cpf)
        cliente.codigo = codigo
        cliente.endereco = endereco
        cliente.telefone = telefone
        cliente.email = email
        return cliente