#-------------------------------------------------
# Configurações do Aplicativo                    |
#-------------------------------------------------

# Configurações do app
from kivy.config import Config

# definindo o tamanho da visualização do app
# Kivy Designer é o que exibe a tela de teste
# Alterando a largura do layout de teste
Config.set("graphics", "width", "400")
Config.set("graphics", "height", "600")


#-------------------------------------------------
# Importações                                    |
#-------------------------------------------------
import kivy # importa o framework
kivy.require('2.3.0') # versão dp kivy a ser usada
from kivy.app import App # componentes principais 
from kivy.uix.label import Label # rótulo
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder # importa as telas

import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder

# carregando o arquivo de telas
Builder.load_file('telas.kv')


#-------------------------------------------------
# Telas da Aplicação                             |
#-------------------------------------------------
# cria a tela do app
class Tela01(Screen):
    pass

#-------------------------------------------------
# Códigos iniciais do App                        |
#-------------------------------------------------
class GerenciadorDeTelas(ScreenManager):
    # Esta classe herda do Gerenciador de telas do kivy
    pass


# classe principal
class MyApp(App):

    # Método principal
    def build(self):
        return GerenciadorDeTelas()

# condição se estiver no Kivy inicia o app
if __name__ == '__main__':
    MyApp().run()