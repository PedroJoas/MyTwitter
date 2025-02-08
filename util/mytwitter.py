from __future__ import annotations

from datetime import datetime
from excecoes import *
from itertools import chain

id_tweet = 0  

def gera_id():
    global id_tweet
    while True:
        id_tweet += 1
        yield id_tweet

class Tweet:
    def __init__(self, usuario: str, mensagem: str) -> None:
        self.__usuario = usuario
        self.__mensagem = mensagem
        self.__data_postagem = datetime.today()
        self.__id_tweet = next(gera_id())
    
    def get_id(self) -> str:
        return self.__id_tweet
    
    def get_usuario(self) -> str:
        return self.__usuario

    def get_mensagem(self) -> str:
        return self.__mensagem
    
    def get_data_postagem(self) -> datetime:
        return self.__data_postagem
    
class Perfil:
    def __init__(self, usuario:str) -> None:
        self.__usuario = usuario
        self.__seguidos = []
        self.__seguidores = []
        self.__tweets = []
        self.__ativo = True
    
    def add_seguidor(self, seguidor:Perfil) -> None:
        self.__seguidores.append(seguidor)
        
    def add_seguidos(self, seguidor: Perfil) -> None:
        self.__seguidos.append(seguidor)
    
    def add_tweet(self, mensagem:str) -> None:
        tweet = Tweet(self.__usuario, mensagem)
        self.__tweets.append(tweet)
    
    def get_tweets(self) -> list:
        return self.__tweets

    def get_tweet(self, id_tweet:int) -> Tweet:
        for tweet in self.__tweets:
            if tweet.get_id() == id_tweet:
                return tweet
        return None
    
    def get_timeline(self) -> list:
        tweets_timelines = [perfil.get_tweets() for perfil in self.__seguidos] + [self.__tweets] # isso serve para não deixar os a lsita heterogenea, ou seja, ter valores e listas
        tweets_timelines = list(chain(*tweets_timelines))
        tweets_timelines.sort(key=lambda x: x.get_data_postagem())

        return tweets_timelines
    
    def set_usuario(self, usuario:str) -> None:
        self.__usuario = usuario
    
    def get_usuario(self) -> str:
        return self.__usuario
    
    def set_ativo(self, ativo:bool) -> None: 
        self.__ativo = ativo
    
    def is_ativo(self) -> bool:
        return self.__ativo
    
    def get_numero_seguidores(self) -> int:
        return len(self.__seguidores)
    
    def get_numero_seguidos(self)-> int:
        return len(self.__seguidos)
     
class PessoaFisica(Perfil):
    def __init__(self, usuario:str, cpf:str) -> None:
        super().__init__(usuario)
        self.__cpf = cpf
    
    def get_cpf(self) -> str:
        return self.__cpf

    def set_cpf(self, novo_cpf) -> None:
        self.__cpf = novo_cpf

class PessoaJuridica(Perfil):
    def __init__(self, usuario:str, cnpj:str) -> None:
        super().__init__(usuario)
        self.__cnpj = cnpj
    
    def get_cnpj(self) -> str:
        return self.__cnpj
    
    def set_cnpj(self, novo_cnpj) -> None:
        self.__cnpj = novo_cnpj
class RepositorioUsuarios:
    def __init__(self) -> None:
        self.__usuarios = []
    
    def cadastrar(self, usuario: Perfil) -> None:
        nome_usuario = usuario.get_usuario()
        usuario_bd = self.buscar(nome_usuario)

        if usuario_bd is not None:
            raise UJCException(nome_usuario)

        self.__usuarios.append(usuario)

    def buscar(self, nome_usuario: str) -> Perfil:
        for usuario in self.__usuarios:
            if nome_usuario == usuario.get_usuario():
                return usuario
        
        return None
    
    def atualizar(self, nome_usuario: str, atributo_modificar:str) -> None:
        usuario = self.buscar(nome_usuario)

        if usuario is None:
            raise UNCException(nome_usuario)
        
        match atributo_modificar:
            case 'nome':
                novo_nome = input('Digite o novo nome: ')
                usuario.set_usuario(novo_nome)
            
            case 'cpf':
                if isinstance(usuario, PessoaFisica):
                    novo_cpf = input('Digite o novo cpf: ')
                    usuario.set_cpf(novo_cpf)
                else:
                    raise UIAAException(usuario.get_usuario())
                
            case 'cnpj':
                if isinstance(usuario, PessoaJuridica):
                    novo_cnpj = input('Digite o novo CNPJ: ')
                    usuario.set_cnpj(novo_cnpj)
                else:
                    raise UIAAException(usuario.get_usuario())
                
            case _:
                raise AIException(usuario.get_usuario())
    
    # PASSIVEL DE MUDANÇA (TIRAR DUVIDA SE ELE DEIXA FAZER DESSA FORMA)
    def get_quantidade_usuarios(self) -> int:
        return len(self.__usuarios)
    
class MyTwitter:
    def __init__(self) -> None:
        self.__repositorio = RepositorioUsuarios()

    def criar_perfil(self,usuario:Perfil) -> None:
        nome_usuario = usuario.get_usuario()
        usuario_bd = self.__repositorio.buscar(nome_usuario)

        if usuario_bd is not None:
            raise PEException(nome_usuario)
        
        self.__repositorio.cadastrar(usuario)
        
    def cancelar_perfil(self, nome_usuario:str) -> None:
        usuario = self.__repositorio.buscar(nome_usuario) # usuario dentro do repositorio

        if usuario is None:
            raise PIException(nome_usuario)
        
        if usuario.is_ativo() == False:
            raise PDException(nome_usuario)

        usuario.set_ativo(False)

    def tweetar(self,nome_usuario:str, mensagem: str) -> None:
        usuario = self.__repositorio.buscar(nome_usuario)
        if usuario is None:
            raise PIException(nome_usuario)
        
        if (len(mensagem) < 1) or (len(mensagem) > 40):
            raise MFPException(nome_usuario)
        
        usuario.add_tweet(mensagem)
    
    def timeline(self,nome_usuario:str) -> list:
        usuario = self.__repositorio.buscar(nome_usuario)
        if usuario is None:
            raise PIException(nome_usuario)
        
        if usuario.is_ativo() == False:
            raise PDException(nome_usuario)    
        
        return usuario.get_timeline()
    
    def tweets(self, nome_usuario:str) -> list:
        usuario = self.__repositorio.buscar(nome_usuario)

        if usuario is None:
            raise PIException(nome_usuario)
    
        if usuario.is_ativo() == False:
            raise PDException(nome_usuario)  

        return usuario.get_tweets()

    def seguir(self, nome_seguidor:str, nome_seguido:str) -> None:
        seguidor = self.__repositorio.buscar(nome_seguidor)
        seguido = self.__repositorio.buscar(nome_seguido)
        if seguidor is None:
            raise PIException(nome_seguidor)
        if seguido is None:
            raise PIException(nome_seguido)
    
        if seguidor.is_ativo() == False:
            raise PDException(nome_seguidor)
        
        if seguido.is_ativo() == False:
            raise PDException(nome_seguido)

        if seguido.get_usuario() == seguidor.get_usuario():
            raise SIException(seguidor.get_usuario())
        
        seguido.add_seguidor(seguidor)
        seguidor.add_seguidos(seguido)

    def numero_seguidores(self, nome_usuario:str) -> int:
        usuario = self.__repositorio.buscar(nome_usuario)

        if usuario is None:
            raise PIException(nome_usuario)
    
        if usuario.is_ativo() == False:
            raise PDException(nome_usuario)

        return usuario.get_numero_seguidores()
    
    def numero_seguidores(self, nome_usuario:str) -> int: 
        usuario = self.__repositorio.buscar(nome_usuario)

        if usuario is None:
            raise PIException(nome_usuario)
    
        if usuario.is_ativo() == False:
            raise PDException(nome_usuario)

        return usuario.get_numero_seguidos() 


if __name__ == '__main__':
    tweet = Tweet('pedro', 'olaa mundo')
    print(tweet.get_id())
    
