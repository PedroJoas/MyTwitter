class UJCException(Exception):
    def __init__(self, nome_usuario, *args):
        self.nome_usuario = nome_usuario
               
        self.__mensagem = "Usuário já cadastrado"
        super().__init__(*args)
    
    def print_mensagem_erro(self):
        print("{}: \nNome Usuario: @{}".format(self.__mensagem, self.nome_usuario))

class UNCException(Exception):
    def __init__(self, nome_usuario, *args):
        self.nome_usuario = nome_usuario
        self.__mensagem = "Usuário não cadastrado"
        super().__init__(*args)
        
    def print_mensagem_erro(self):
        print("{}: \nNome Usuario: @{}".format(self.__mensagem,self.nome_usuario))
        

class PIException(Exception):
    def __init__(self, nome_usuario, *args):
        self.__nome_usuario = nome_usuario
        self.__mensagem = "Perfil Inexistente"
        super().__init__(*args)
    
    def print_mensagem_erro(self):
        print("{}: \nNome Usuario @{}".format(self.__mensagem,self.__nome_usuario))

class MFPException(Exception):
    def __init__(self, nome_usuario, *args):
        self.__nome_usuario = nome_usuario
        self.__mensagem = "Mensagem fora do padrão"
        super().__init__(*args)

    def print_mensagem_erro(self):
        print("{}: \nNome Usuario @{}.".format(self.__mensagem,self.__nome_usuario))

class PDException(Exception):
    def __init__(self, nome_usuario, *args):
        self.__nome_usuario = nome_usuario
        self.__mensagem = "Perfil desativado"
        super().__init__(*args)

    def print_mensagem_erro(self):
        print("{}: \nNome Usuario @{}.".format(self.__mensagem, self.__nome_usuario))

class PEException(Exception):
    def __init__(self, nome_usuario, *args):
        self.__nome_usuario = nome_usuario
        self.__mensagem = "Usuário já cadastrado"
        super().__init__(*args)

    def print_mensagem_erro(self):
        print("{}: \nNome Usuario @{}.".format(self.__mensagem, self.__nome_usuario))

class SIException(Exception):
    def __init__(self, nome_usuario, *args):
        self.__nome_usuario = nome_usuario
        self.__mensagem = "Seguidor inválido"
        super().__init__(*args)

    def print_mensagem_erro(self):
        print("{}: \nNome Usuario @{} tentou se seguir.".format(self.__mensagem, self.__nome_usuario))

class UIAAException(Exception):
    def __init__(self, nome_usuario, *args):
        self.__nome_usuario = nome_usuario
        self.__mensagem = "Usuário impossibilitado de alterar atributo"
        super().__init__(*args)

    def print_mensagem_erro(self):
        print("{}: \nNome Usuario @{}.".format(self.__mensagem, self.__nome_usuario))

class AIException(Exception):
    def __init__(self, nome_usuario, *args):
        self.__nome_usuario = nome_usuario
        self.__mensagem = "Atributo inexistente"
        super().__init__(*args)

    def print_mensagem_erro(self):
        print("{}: \nNome Usuario @{}.".format(self.__mensagem, self.__nome_usuario))
