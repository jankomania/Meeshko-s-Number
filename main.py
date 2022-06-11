version = 0.1

from enum import auto
import random
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty


#Window.fullscreen = 'auto'


class Game():
    def __init__(self, difficulty='Medium', lives='10', level='0', score=0, label_from='0', label_to='0', curr='0') -> None:
        self.difficulty = difficulty
        self.lives = lives
        self.level = level
        self.score = score
        self.label_from = label_from
        self.label_to = label_to
        self.curr = curr

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
    label_score = ObjectProperty(None)
    label_to = ObjectProperty(None)
    
    lives_flag = True

    def update_lives(self):
        self.label_lives.text = game.lives


    def one(self):
        if self.label_input.text in ['HIGHER', 'LOWER']:
            self.label_input.text = ''

        if len(self.label_input.text) > 7: pass
        elif self.label_input.text == '':
            self.label_input.text = '1'
        else: self.label_input.text += '1'
        
        
    def two(self):
        if self.label_input.text in ['HIGHER', 'LOWER']:
            self.label_input.text = ''
        
        if len(self.label_input.text) > 7: pass
        elif self.label_input.text == '':
            self.label_input.text = '2'
        else: self.label_input.text += '2'
        
        
    def three(self):
        if self.label_input.text in ['HIGHER', 'LOWER']:
            self.label_input.text = ''
        
        if len(self.label_input.text) > 7: pass
        elif self.label_input.text == '':
            self.label_input.text = '3'
        else: self.label_input.text += '3'
        
        
    def four(self):
        if self.label_input.text in ['HIGHER', 'LOWER']:
            self.label_input.text = ''

        if len(self.label_input.text) > 7: pass
        elif self.label_input.text == '':
            self.label_input.text = '4'
        else: self.label_input.text += '4'
        
        
    def five(self):
        if self.label_input.text in ['HIGHER', 'LOWER']:
            self.label_input.text = ''

        if len(self.label_input.text) > 7: pass
        elif self.label_input.text == '':
            self.label_input.text = '5'
        else: self.label_input.text += '5'
        
        
    def six(self):
        if self.label_input.text in ['HIGHER', 'LOWER']:
            self.label_input.text = ''

        if len(self.label_input.text) > 7: pass
        elif self.label_input.text == '':
            self.label_input.text = '6'
        else: self.label_input.text += '6'
        
        
    def seven(self):
        if self.label_input.text in ['HIGHER', 'LOWER']:
            self.label_input.text = ''

        if len(self.label_input.text) > 7: pass
        elif self.label_input.text == '':
            self.label_input.text = '7'
        else: self.label_input.text += '7'
        
        
    def eight(self):
        if self.label_input.text in ['HIGHER', 'LOWER']:
            self.label_input.text = ''

        if len(self.label_input.text) > 7: pass
        elif self.label_input.text == '':
            self.label_input.text = '8'
        else: self.label_input.text += '8'
        
    
    def nine(self):
        if self.label_input.text in ['HIGHER', 'LOWER']:
            self.label_input.text = ''

        if len(self.label_input.text) > 7: pass
        elif self.label_input.text == '':
            self.label_input.text = '9'
        else: self.label_input.text += '9'
        
        
    def zero(self):
        if self.label_input.text in ['HIGHER', 'LOWER']:
            self.label_input.text = ''

        if len(self.label_input.text) > 7: pass
        elif self.label_input.text == '':
            self.label_input.text = '0'
        else: self.label_input.text += '0'
        
        
    def delete(self):
        if self.label_input.text != '':
            self.label_input.text = self.label_input.text[:-1]
        

    def submit(self):
        #game.printr()
        if self.label_input.text in ['', 'HIGHER', 'LOWER']:
            self.label_input.text = ''
            return 1
        
        if self.lives_flag:
            self.lives_flag = False
            self.label_lives.text = game.lives
        
        if self.label_input.text == str(game.curr):
            game.lives = str(int(int(game.lives) * 1.25))
            self.label_lives.text = game.lives
            
            self.label_input.text = ''
            
            if game.score == 0:
                    game.score = 100
            elif game.score < 0:
                if game.difficulty == 'Easy':
                    game.score = int(game.score / 1.25)
                elif game.difficulty == 'Medium':
                    game.score = int(game.score / 2)
                else: game.score = int(game.score / 2.5)
            else:
                if game.difficulty == 'Easy':
                    game.score = int(game.score * 1.75)
                elif game.difficulty == 'Medium':
                    game.score = int(game.score * 2)
                else: game.score = int(game.score * 2.5)

            self.label_to.text = str(int(self.label_to.text) * 2)
            game.curr = random.randint(0, int(self.label_to.text))
        else:
            if game.score < 10000:
                game.score -= 100
            elif game.score < 100000:
                game.score -= 1000
            else: game.score -= 10000

            if game.lives == '1':
                self.label_lives.text = 'DEAD'
                return 1
            else:
                game.lives = str(int(game.lives) - 1)
                self.label_lives.text = str(game.lives)

            if int(self.label_input.text) < game.curr:
                self.label_input.text = 'HIGHER'
            else: self.label_input.text = 'LOWER'

        self.label_score.text = str(game.score)
        print(game.curr)


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
