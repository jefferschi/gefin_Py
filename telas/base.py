# a ideia é tentar fazer como em models. verificar sobre a notação @abstractmethod se preciso mesmo usar
# ou se posso fazer como em models, aparentemente funciona e é mais simples. Creio que com notação é obrigado
# a usar o método

# tentar usar com o fornecedor primeiro.

class BaseTelaCad:
    def __init__(self) -> None:
        pass




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