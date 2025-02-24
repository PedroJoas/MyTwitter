import time
import threading
from util.mytwitter import *
import random
import traceback
from util.excecoes import *

lock = threading.Lock()

def instancia_perfis():
    perfis_objetos = []
    with open('dados/usuarios.txt') as f:
        for linha in f:
            perfil = linha.strip('\n').split(',')
            if len(perfil) == 1:
                perfil_objeto = Perfil(perfil[0])
            elif '/' in perfil[1]:
                perfil_objeto = PessoaJuridica(perfil[0], perfil[1])
            else:
                perfil_objeto = PessoaFisica(perfil[0], perfil[1])
            
            perfis_objetos.append(perfil_objeto)
    
    return perfis_objetos

def retorna_tweet():
    with open('dados/tweets.txt') as f:
        tweet_aleatorio = random.choice(f.readlines()).strip('\n')

    return tweet_aleatorio

def rotina(mytwitter: MyTwitter, usuario: Perfil):
    nome_usuario = usuario.get_usuario()
    intervalo_de_espera = random.randint(0,3)
    # SEGUIR ALGUÉM ALEATÓRIO
    with open('dados/usuarios.txt') as f:
        linhas = f.readlines()
        usuario_seguido = random.choice(linhas).strip('\n').split(',')[0]
        try:
            mytwitter.seguir(nome_usuario, usuario_seguido)
        except SIException as sie:
            sie.print_mensagem_erro()
        except PIException as pie:
            pie.print_mensagem_erro()
        except PDException as pde:
            pde.print_mensagem_erro()
        else:
            print(f'{nome_usuario} começou a seguir {usuario_seguido}')

    time.sleep(intervalo_de_espera)

    # TWEETAR
    try:
        mytwitter.tweetar(nome_usuario, retorna_tweet())
    except MFPException as mfpe:
        mfpe.print_mensagem_erro()
    except PIException as pie:
        pie.print_mensagem_erro()

    # TIMELINE
    with lock:
        print(f'Timeline do usuario {nome_usuario}:')
        try:
            timeline = mytwitter.timeline(nome_usuario)
        except PIException as pie:
            pie.print_mensagem_erro()
        except PDException as pde:
            pde.print_mensagem_erro()
        else:
            for tweet in timeline:
                print(f'@{tweet.get_usuario()}: {tweet.get_mensagem()} -- {tweet.get_data_postagem()}')

        print('---'*20)

    # TWEETAR DNV
    time.sleep(intervalo_de_espera)
    try:
        mytwitter.tweetar(nome_usuario, f'eu sou {nome_usuario} dnv')
    except MFPException as mfpe:
        mfpe.print_mensagem_erro()
    except PIException as pie:
        pie.print_mensagem_erro()

    with lock:
        print(f'Timeline do usuario {nome_usuario}:')
        try:
            timeline = mytwitter.timeline(nome_usuario)
        except PIException as pie:
            pie.print_mensagem_erro()
        except PDException as pde:
            pde.print_mensagem_erro()
        else:
            for tweet in timeline:
                print(f'@{tweet.get_usuario()}: {tweet.get_mensagem()} -- {tweet.get_data_postagem()}')

        print('---'*20)
    
    if random.randint(1,5) == 3:
        try:
            mytwitter.cancelar_perfil(nome_usuario)
        except PIException as pie:
            pie.print_mensagem_erro()
        except PDException as pde:
            pde.print_mensagem_erro()
        else:
            print(f'Usuario @{nome_usuario} cancelou o perfil :('+'\n'+'-'*20)



perfis_objetos = instancia_perfis()
mytwitter = MyTwitter()
threads = []
for perfil in perfis_objetos:
    try:
        mytwitter.criar_perfil(perfil)
        t = threading.Thread(target=rotina, args=(mytwitter, perfil))
        threads.append(t)
    except PEException as pee:
        pee.print_mensagem_erro()

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()


