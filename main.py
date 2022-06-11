version = 0.1

import random
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty


#Window.fullscreen = True


class Game():
    def __init__(self, difficulty='Medium', lives='10', level='0', score=0, label_from='0', label_to='0', curr='0') -> None:
        self.difficulty = difficulty
        self.lives = lives
        self.level = level
        self.score = score
        self.label_from = label_from
        self.label_to = label_to
        self.curr = curr


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


class GameWin(Screen):
    base_score = 100

    label_input = ObjectProperty(None)
    label_lives = ObjectProperty(None)
    label_score = ObjectProperty(None)
    label_to = ObjectProperty(None)

    num_btn = StringProperty()
    
    lives_flag = True


    def btn_input(self):
        # Clears the input label if it contains either the high or low guess hint
        if self.label_input.text in ['HIGHER', 'LOWER']:
            self.label_input.text = ''

        # Limits the input label to 7 digits and concatenates the last pressed button
        if len(self.label_input.text) > 7: pass
        elif self.label_input.text == '':
            self.label_input.text = self.num_btn
        else:
            self.label_input.text += self.num_btn

    
    def check_input(self):
        # Prevents blank and hint input
        if self.label_input.text in ['', 'HIGHER', 'LOWER']:
            self.label_input.text = ''
            return True


    def update_lives(self):
        # Updates the lives label on the first guess
        self.lives_flag = False
        self.label_lives.text = game.lives


    def hint(self):
        # Hints on the weight of the current number
        if self.label_input.text > game.curr:
            self.label_input.text = 'HIGHER'
        else:
            self.label_input.text = 'LOWER'

        # Takes away lives and score
        if game.score < 0:
            if game.level < 15:
                game.score -= 100
            else: game.score *= 2
        else:
            if game.level < 15:
                game.score -= 100
            else: game.score /= 2

        if game.lives != '1':
            game.lives -= 1
        else: game.lives = 'DEAD'


    def score(self):
        # Gives score appropriate to the current level and difficulty
        if game.difficulty == 'Easy':
            if game.level < '5':
                game.score += 100
            elif game.level < '10':
                game.score += 500
            elif game.level < '15':
                game.score += 1000
            else: game.score *= 2
        elif game.difficulty == 'Medium':
            if game.level < '5':
                game.score += 200
            elif game.level < '10':
                game.score += 1000
            elif game.level < '15':
                game.score += 2000
            else: game.score *= 4
        else:
            if game.level < '5':
                game.score += 500
            elif game.level < '10':
                game.score += 2500
            elif game.level < '15':
                game.score += 5000
            else: game.score *= 10
        


    def generate(self):
        # Meeshko kidnaps a new number
        self.label_to.text = str(int(self.label_to.text) * 2)
        game.curr = random.randint(0, int(self.label_to.text))


    def update(self):
        # Updates score and lives labels
        self.label_score.text = game.score
        self.label_lives.text = game.lives

        
    def delete(self):
        if self.label_input.text != '':
            self.label_input.text = self.label_input.text[:-1]
        

    def submit(self):
        if self.check_input():
            pass
        else:
            # Checks if the guess is correct and calls score() function
            if self.label_input.text == game.curr:
                self.score()
                self.generate()
            else:
                self.hint()

        self.update()

        if self.lives_flag:
            self.update_lives()

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
