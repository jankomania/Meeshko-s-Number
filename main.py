version = 0.1

import time
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty

class Game():
    def __init__(self, difficulty='Medium', lives='10', level='0', score='0', label_from='0', label_to='0') -> None:
        self.difficulty = difficulty
        self.lives = lives
        self.level = level
        self.score = score
        self.label_from = label_from
        self.label_to = label_to

    def printr(self):
        print(self.difficulty)
        print(self.lives)
        print(self.level)
        print(self.score)
        print(self.label_from)
        print(self.label_to)


game = Game()


class MainMenu(Screen):
    def easy(self):
        game.difficulty = 'Easy'
        game.lives = '20'

    def med(self):
        game.difficulty = 'Medium'
        game.lives = '10'


    def hard(self):
        game.difficulty = 'Hard'
        game.lives = '5'

    def printr(self):
        game.printr()

    def start_game(self):
        if game.difficulty == 'Easy': game.lives = '20'
        elif game.difficulty == 'Medium': game.lives = '10'
        else: game.lives == '5'


class GameWin(Screen):
    label_input = ObjectProperty(None)
    label_lives = ObjectProperty(None)

    def update_lives(self):
        self.label_lives.text = game.lives


    def one(self):
        if len(self.label_input.text) > 7: pass
        elif self.label_input.text == '':
            self.label_input.text = '1'
        else: self.label_input.text += '1'
        
        
    def two(self):
        if len(self.label_input.text) > 7: pass
        elif self.label_input.text == '':
            self.label_input.text = '2'
        else: self.label_input.text += '2'
        
        
    def three(self):
        if len(self.label_input.text) > 7: pass
        elif self.label_input.text == '':
            self.label_input.text = '3'
        else: self.label_input.text += '3'
        
        
    def four(self):
        if len(self.label_input.text) > 7: pass
        elif self.label_input.text == '':
            self.label_input.text = '4'
        else: self.label_input.text += '4'
        
        
    def five(self):
        if len(self.label_input.text) > 7: pass
        elif self.label_input.text == '':
            self.label_input.text = '5'
        else: self.label_input.text += '5'
        
        
    def six(self):
        if len(self.label_input.text) > 7: pass
        elif self.label_input.text == '':
            self.label_input.text = '6'
        else: self.label_input.text += '6'
        
        
    def seven(self):
        if len(self.label_input.text) > 7: pass
        elif self.label_input.text == '':
            self.label_input.text = '7'
        else: self.label_input.text += '7'
        
        
    def eight(self):
        if len(self.label_input.text) > 7: pass
        elif self.label_input.text == '':
            self.label_input.text = '8'
        else: self.label_input.text += '8'
        
    
    def nine(self):
        if len(self.label_input.text) > 7: pass
        elif self.label_input.text == '':
            self.label_input.text = '9'
        else: self.label_input.text += '9'
        
        
    def zero(self):
        if len(self.label_input.text) > 7: pass
        elif self.label_input.text == '':
            self.label_input.text = '0'
        else: self.label_input.text += '0'
        
        
    def delete(self):
        if self.label_input.text != '':
            self.label_input.text = self.label_input.text[:-1]
        

    def submit(self):
        game.printr()


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('style.kv')


class MeeshkosNumberApp(App):
    def build(self):
        sm = ScreenManager()
        self.first_screen = MainMenu(name='Main Menu')
        self.sec_screen = GameWin(name='Game Window')
        sm.add_widget(self.first_screen)
        sm.add_widget(self.sec_screen)

        return sm


if __name__ == '__main__':
    MeeshkosNumberApp().run()
