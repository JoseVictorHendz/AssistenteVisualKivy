import kivy
from kivy.app import App
from kivy.core.window import Window
from  kivy.utils import get_color_from_hex as c
from kivy.uix.screenmanager import ScreenManager, Screen
import pygame
pygame.init()
kivy.require('1.8.0')
__version__ = "0.1"
Window.clearcolor = c("#FFFFFF")

class TelaMenu(Screen):
    pass

class UsuarioNome(Screen):
     pass

class UsuarioEmail(Screen):
    pass

class ScreenManagement(ScreenManager):
    def switch_to_telaMenu(self):
        self.current = 'telaMenu'

    def switch_to_usuarioNome(self):
        self.current = 'usuarioNome'

    def switch_to_usuarioEmail(self):
        self.current = 'usuarioEmail'
    def som(self):
        # pygame.init()
        # pygame.mixer.music.load('bemVindo.mp3')
        # pygame.event.wait()
        pass

class MenuApp(App):
    def build(self):
        self.root = ScreenManagement()
        return self.root




# if __name__ == '__main__':
MenuApp().run()