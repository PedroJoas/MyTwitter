from mytwitter import *
import mytwitter # Isso ajuda a chamar a variavel global sem fazer uma copia
from datetime import datetime
from time import sleep

import unittest
from unittest.mock import patch

class TestTweet(unittest.TestCase):

    def setUp(self): # método que reinicializa a variável global
        mytwitter.id_tweet = 0
    
    def test_id(self):
        tweet = Tweet('lincolnsrocha', 'Tweetando guys')
        id = tweet.get_id()

        self.assertEqual(id, 1, 'Erro no incremento do id')
        
    def test_nome_tweet(self):
        tweet = Tweet('lincolnsrocha', 'Tweetando guys')
        nome_usuario = tweet.get_usuario()
        self.assertEqual(nome_usuario, 'lincolnsrocha', 'Erro no nome do tweet')

    def test_mensagem(self):
        tweet = Tweet('lincolnsrocha', 'Tweetando guys')
        self.assertEqual(tweet.get_mensagem(), 'Tweetando guys', 'Erro na mensagem')
    
    def test_data_postagem(self):
        tweet = Tweet('lincolnsrocha', 'Tweetando guys')
        self.assertIsInstance(tweet.get_data_postagem(), datetime, 'Erro no tipo da data de postagem')

class TestPerfil(unittest.TestCase):
    def setUp(self):
        mytwitter.id_tweet = 0 # reinicia a variavel a cada teste

    def test_inicializa_seguidores(self):
        usuario = Perfil('lincolnsrocha')
        self.assertEqual(usuario.get_numero_seguidores(), 0, 'Erro na inicialização da variavel seguidores')
    
    def test_inicializa_seguidos(self):
        usuario = Perfil('lincolnsrocha')
        self.assertEqual(usuario.get_numero_seguidos(), 0, 'Erro na inicialização da variavel seguidos')

    def test_inicializa_tweets(self):
        usuario = Perfil('lincolnsrocha')
        self.assertEqual(len(usuario.get_tweets()), 0, 'Erro na inicialização da variavel tweets')
    
    def test_inicializa_ativo(self):
        usuario = Perfil('lincolnsrocha')
        self.assertEqual(usuario.is_ativo(), True, 'Erro na inicialização da variável ativo')

    def test_add_seguidor(self):
        usuario1 = Perfil('lincolnsrocha')
        usuario2 = Perfil('pedrojoas')
        usuario1.add_seguidor(usuario2)
        self.assertEqual(usuario1.get_numero_seguidores(), 1, 'Erro na inserção de seguidores')

    def test_add_seguidos(self):
        usuario1 = Perfil('lincolnsrocha')
        usuario2 = Perfil('pedrojoas')
        usuario1.add_seguidos(usuario2)
        self.assertEqual(usuario1.get_numero_seguidos(), 1, 'Erro na inserção de seguidos')
    
    def test_add_tweet(self):
        usuario = Perfil('lincolnsrocha')
        usuario.add_tweet('Tweetando guys')
        self.assertEqual(len(usuario.get_tweets()), 1, 'Erro na inserção de tweets')

    def test_get_tweet(self):
        usuario = Perfil('lincolnsrocha')
        usuario.add_tweet('Tweetando guys')
        tweet = usuario.get_tweet(1)
        self.assertEqual(tweet.get_mensagem(), 'Tweetando guys', 'Erro em recuperar o tweet')

    def test_get_timeline(self):
        usuario1 = Perfil('lincolnsrocha')
        usuario2 = Perfil('pedrojoas')

        usuario1.add_seguidos(usuario2)

        usuario1.add_tweet('Tweetando guys')
        usuario2.add_tweet('To vendo tweets')

        timeline = usuario1.get_timeline()

        self.assertEqual(len(timeline), 2, 'Erro no incremento na timeline')
    
    def test_verifica_ordenacao_timeline(self):
        usuario1 = Perfil('lincolnsrocha')
        usuario2 = Perfil('pedrojoas')

        usuario1.add_seguidos(usuario2)

        usuario1.add_tweet('Tweetando guys')
        sleep(1)
        usuario2.add_tweet('To vendo tweets')

        timeline = usuario1.get_timeline()
        primeiro_tweet = timeline[0]
        segundo_tweet = timeline[1]
        self.assertTrue(primeiro_tweet.get_data_postagem() <= segundo_tweet.get_data_postagem(), 'Erro na ordenação da timeline')
    
    def test_set_nome(self):
        usuario = Perfil('lincolnsrocha')

        usuario.set_usuario('pedrojoas')
        self.assertEqual(usuario.get_usuario(), 'pedrojoas', 'Erro ao mudar o nome de usuário')

    def test_set_ativo(self):
        usuario = Perfil('lincolnsrocha')

        usuario.set_ativo(False)

        self.assertEqual(usuario.is_ativo(), False, 'Erro ao trocar a variável ativo')
    
    
class TestePessoaFisica(unittest.TestCase):

    def test_get_cpf(self):
        usuario = PessoaFisica('lincolnsrocha', '129.791.191-86')
        
        self.assertEqual(usuario.get_cpf(), '129.791.191-86', 'Erro na inserção do cpf')

class TestPessoaJuridica(unittest.TestCase):

    def test_get_cnpj(self):
        usuario = PessoaJuridica('pepsico', '31.565.104/0021-10')
        
        self.assertEqual(usuario.get_cnpj(), '31.565.104/0021-10', 'Erro na inserção do cnpj')

class TestRepositorioUsuarios(unittest.TestCase):

    def test_inicializa_usuarios(self):
        repositorio = RepositorioUsuarios()
        self.assertEqual(repositorio.get_quantidade_usuarios(), 0, 'Erro na inicialização da variável usuarios')

    def test_cadastrar(self):
        repositorio = RepositorioUsuarios()
        usuario = Perfil('lincolnsrocha')
        repositorio.cadastrar(usuario)

        self.assertEqual(repositorio.get_quantidade_usuarios(), 1, 'Erro no cadastro de usuarios')

    def test_buscar(self):
        repositorio = RepositorioUsuarios()
        usuario = Perfil('lincolnsrocha')
        repositorio.cadastrar(usuario)
        usuario_buscado = repositorio.buscar('lincolnsrocha')

        self.assertIsNotNone(usuario_buscado, 'Erro ao buscar usuário')

    @patch("builtins.input", return_value="pedroflima")  # Simulando entrada do usuário
    def test_atualizar_nome(self, mock_input):
        repositorio = RepositorioUsuarios()
        usuario = Perfil('lincolnsrocha')
        repositorio.cadastrar(usuario)
        repositorio.atualizar('lincolnsrocha', 'nome')
        self.assertEqual(usuario.get_usuario(), 'pedroflima', 'Erro ao atualizar o nome de usuario')
    
    @patch("builtins.input", return_value="129.791.191-86")  # Simulando entrada do usuário
    def test_atualizar_cpf(self, mock_input):
        repositorio = RepositorioUsuarios()
        usuario = PessoaFisica('lincolnsrocha', '000.000.000-00')
        repositorio.cadastrar(usuario)
        repositorio.atualizar('lincolnsrocha', 'cpf')
        self.assertEqual(usuario.get_cpf(), '129.791.191-86', 'Erro ao atualizar o cpf do usuario')

    @patch("builtins.input", return_value="31.565.104/0021-10")  # Simulando entrada do usuário
    def test_atualizar_cnpj(self, mock_input):
        repositorio = RepositorioUsuarios()
        usuario = PessoaJuridica('pepsico', '00.000.000/0000-00')
        repositorio.cadastrar(usuario)
        repositorio.atualizar('pepsico', 'cnpj')
        self.assertEqual(usuario.get_cnpj(), '31.565.104/0021-10', 'Erro ao atualizar o cnpj do usuario')


class TestMyTwitter(unittest.TestCase):
    
    def testCriarPerfil(self):
        mytwitter = MyTwitter()
        usuario = Perfil('lincolnsrocha')
        mytwitter.criar_perfil(usuario)
        seguidores = mytwitter.numero_seguidores('lincolnsrocha')
        self.assertEqual(seguidores, 0, 'Erro ao cadastrar usuário')
    
    def testCancelarPerfil(self):
        mytwitter = MyTwitter()
        usuario = Perfil('lincolnsrocha')
        mytwitter.criar_perfil(usuario)
        mytwitter.cancelar_perfil('lincolnsrocha')
        
        self.assertEqual(usuario.is_ativo(), False, 'Erro ao cancelar perfil')

    def testSeguir(self):
        mytwitter = MyTwitter()
        usuario1 = Perfil('lincolnsrocha')
        usuario2 = Perfil('pedrojoas')

        mytwitter.criar_perfil(usuario1)
        mytwitter.criar_perfil(usuario2)

        mytwitter.seguir('lincolnsrocha', 'pedrojoas')

        seguidores = mytwitter.numero_seguidores('pedrojoas')
        seguindo = mytwitter.numero_seguidos('lincolnsrocha')

        self.assertEqual(seguidores, 1, 'Erro ao adicionar seguidor')
        self.assertEqual(seguindo, 1, 'Erro ao adicionar seguidos')
    
    
        

if __name__ == '__main__':
    unittest.main()