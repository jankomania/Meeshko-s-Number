__version__ = 0.1

import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty

class Game():
    def __init__(self, difficulty='Medium', start_gold='1000') -> None:
        self.difficulty = difficulty
        self.start_gold = start_gold


    def printr(self):
        print(self.difficulty)
        print(self.start_gold)


game = Game()


class MainMenu(Screen):
    difficulty = ObjectProperty('Medium')
    start_gold = ObjectProperty(1000)

    def easy(self):
        game.difficulty = 'Easy'
        game.start_gold = '500'

    def med(self):
        game.difficulty = 'Medium'
        game.start_gold = '1000'

    def hard(self):
        game.difficulty = 'Hard'
        game.start_gold = '1500'

    def printr(self):
        game.printr()


class GameWin(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('style.kv')


class MeeshkosNumberApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    MeeshkosNumberApp().run()
