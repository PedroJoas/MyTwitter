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
    
    def add_seguidor(self, seguidor:Perfil):
        self.__seguidores.append(seguidor)
        
    def add_seguidos(self, seguidor: Perfil):
        self.__seguidos.append(seguidor)
    
    def add_tweet(self, mensagem:str):
        if (len(mensagem) < 1) or (len(mensagem) > 40):
            raise MFPException(self.__usuario)
        
        tweet = Tweet(self.__usuario, mensagem)
        self.__tweets.append(tweet)
    
    def get_tweets(self):
        return self.__tweets

    def get_tweet(self, id_tweet):
        for tweet in self.__tweets:
            if tweet.get_id() == id_tweet:
                return tweet
    
    def get_timeline(self):
        pass

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
    
    def cadastrar(self, usuario: Perfil):
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

class MyTwitter:
    def __init__(self):
        self.__repositorio = RepositorioUsuarios()

    def criar_perfil(self,usuario:Perfil):
        self.__repositorio.cadastrar(usuario)
        
    def cancelar_perfil(self, usuario:Perfil):
        nome_usuario = usuario.get_usuario()
        usuario_bd = self.__repositorio.buscar(nome_usuario)
        # CONTINUAR NO RESTO DA IMPLEMENTAÇÃO

    def tweetar(self,nome_usuario:str, mensagem: str):
        usuario = self.__repositorio.buscar(nome_usuario)
        if usuario is None:
            raise PIException(nome_usuario)
        
        usuario.add_tweet(mensagem)
    
    def timeline(self,nome_usuario:str):
        usuario = self.__repositorio.buscar(nome_usuario)
        # CONTINUAR NO RESTO DA IMPLEMENTAÇÃO
    
    def tweets(self, nome_usuario:str):
        usuario = self.__repositorio.buscar(nome_usuario)
        # CONTINUAR NO RESTO DA IMPLEMENTAÇÃO
    
    def seguir(self, seguidor:str, seguido:str):
        seguidor = self.__repositorio.buscar(seguidor)
        seguido = self.__repositorio.buscar(seguido)
        # CONTINUAR NO RESTO DA IMPLEMENTAÇÃO
    
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
        
    
