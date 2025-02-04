from datetime import datetime
from __future__ import annotations
from excecoes import *

id_tweet = 0  

def gera_id():
    global id_tweet
    while True:
        id_tweet += 1
        yield id_tweet

class Tweet:
    def __init__(self, usuario: str, mensagem: str):
        self.__usuario = usuario
        self.__mensagem = mensagem
        self.__data_postagem = datetime.today()
        self.__id_tweet = next(gera_id())
    
    def get_id(self) -> str:
        return self.__id_tweet
    
    def get_usuario(self):
        return self.__usuario

    def get_mensagem(self):
        return self.__mensagem
    
    def get_data_postagem(self):
        return self.__data_postagem
    
class Perfil:
    def __init__(self, usuario:str):
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

    def get_tweet(self, id_tweet) -> Tweet:
        for tweet in self.__tweets:
            if tweet.get_id() == id_tweet:
                return tweet
        return None
    
    def get_timeline(self):
        tweets_timelines = [perfil.get_tweets() for perfil in self.__seguidos] + self.__tweets
        tweets_timelines.sort(key=lambda x: x.get_data_postagem())

        return tweets_timelines
    
    def set_usuario(self, usuario):
        self.__usuario = usuario
    
    def get_usuario(self):
        return self.__usuario
    
    def set_ativo(self, ativo:bool):
        self.__ativo = ativo
    
    def is_ativo(self):
        return self.__ativo
    
    def get_numero_seguidores(self):
        return len(self.__seguidores)
    
    def get_numero_seguidos(self):
        return len(self.__seguidos)
     
class PessoaFisica(Perfil):
    def __init__(self, usuario:str, cpf:str):
        super(usuario)
        self.__cpf = cpf
    
    def get_cpf(self):
        return self.__cpf

class PessoaJuridica(Perfil):
    def __init__(self, usuario, cnpj):
        super(usuario)
        self.__cnpj = cnpj
    
    def get_cnpj(self):
        return self.__cnpj
    
class RepositorioUsuarios:
    def __init__(self):
        self.__usuarios = []
    
    def cadastrar(self, usuario: Perfil) -> None:
        nome_usuario = usuario.get_usuario()
        usuario_bd = self.buscar(nome_usuario)

        if usuario_bd is not None:
            raise UJCException(nome_usuario)

        self.__usuarios.append(usuario)

    def buscar(self, nome_usuario: str):
        for usuario in self.__usuarios:
            if nome_usuario == usuario.get_usuario():
                return usuario
        
        return None
    
    def atualizar(self, nome_usuario: str):
        usuario = self.buscar(nome_usuario)

        if usuario is None:
            raise UNCException(nome_usuario)
        
        # CONTINUAR NO RESTO DA IMPLEMENTAÇÃO
        # TIRAR DÚVIDA SOBRE ESSE MÉTODO EM ESPECÍFICO
    
    # PASSIVEL DE MUDANÇA (TIRAR DUVIDA SE ELE DEIXA FAZER DESSA FORMA)
    def get_quantidade_usuarios(self):
        return len(self.__usuarios)
    
class MyTwitter:
    def __init__(self):
        self.__repositorio = RepositorioUsuarios()

    def criar_perfil(self,usuario:Perfil):
        nome_usuario = usuario.get_usuario()
        usuario_bd = self.__repositorio.buscar(nome_usuario)

        if usuario_bd is not None:
            raise PEException(nome_usuario)
        
        self.__repositorio.cadastrar(usuario)
        
    def cancelar_perfil(self, nome_usuario:str):
        usuario = self.__repositorio.buscar(nome_usuario) # usuario dentro do repositorio

        if usuario is None:
            raise PIException(nome_usuario)
        
        if usuario.is_ativo() == False:
            raise PDException(nome_usuario)

        usuario.set_ativo(False)

    def tweetar(self,nome_usuario:str, mensagem: str):
        usuario = self.__repositorio.buscar(nome_usuario)
        if usuario is None:
            raise PIException(nome_usuario)
        
        if (len(mensagem) < 1) or (len(mensagem) > 40):
            raise MFPException(nome_usuario)
        
        usuario.add_tweet(mensagem)
    
    def timeline(self,nome_usuario:str):
        usuario = self.__repositorio.buscar(nome_usuario)
        if usuario is None:
            raise PIException(nome_usuario)
        
        if usuario.is_ativo() == False:
            raise PDException(nome_usuario)    
        
        return usuario.get_timeline()
    
    def tweets(self, nome_usuario:str):
        usuario = self.__repositorio.buscar(nome_usuario)

        if usuario is None:
            raise PIException(nome_usuario)
    
        if usuario.is_ativo() == False:
            raise PDException(nome_usuario)  

        return usuario.get_tweets()

    def seguir(self, nome_seguidor:str, nome_seguido:str):
        seguidor = self.__repositorio.buscar(nome_seguidor)
        seguido = self.__repositorio.buscar(nome_seguido)
        # CONTINUAR NO RESTO DA IMPLEMENTAÇÃO
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
        
        seguido.add_seguidores(seguidor)
        seguidor.add_seguidos(seguido)

    def numero_seguidores(self, nome_usuario:str):
        usuario = self.__repositorio.buscar(nome_usuario)

        if usuario is None:
            raise PIException(nome_usuario)
    
        if usuario.is_ativo() == False:
            raise PDException(nome_usuario)

        return usuario.get_numero_seguidores()
    
    def numero_seguidores(self, nome_usuario:str):
        usuario = self.__repositorio.buscar(nome_usuario)

        if usuario is None:
            raise PIException(nome_usuario)
    
        if usuario.is_ativo() == False:
            raise PDException(nome_usuario)

        return usuario.get_numero_seguidos() 
        
    
