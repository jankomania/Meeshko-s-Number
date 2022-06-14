version = 0.1

import random

import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty


Window.fullscreen = 'auto'

class Game():
    def __init__(self, difficulty='Medium', lives=5, level=0, score=0, label_from='0', label_to='0', curr=0) -> None:
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
        game.lives = 15

    def med(self):
        game.difficulty = 'Medium'
        game.lives = 5

    def hard(self):
        game.difficulty = 'Hard'
        game.lives = 5


class GameWin(Screen):
    base_score = 100

    label_input = ObjectProperty(None)
    label_lives = ObjectProperty(None)
    label_level = ObjectProperty(None)
    label_score = ObjectProperty(None)
    label_to = ObjectProperty(None)

    num_btn = StringProperty()
    
    lives_flag = True

    def __init__(self, **kw):
        super(GameWin).__init__(**kw):
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)


    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None


    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        pass


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
        self.label_lives.text = str(game.lives)


    def hint(self):
        # Hints on the weight of the current number
        if int(self.label_input.text) < game.curr:
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

        if game.lives != 1:
            game.lives -= 1
        else: game.lives = -2345678


    def score(self):
        # Gives score and lives appropriate to the current level and difficulty
        game.score = int(float(game.score))

        if game.difficulty == 'Easy':
            if game.level < 5:
                game.lives += 10
                self.base_score = self.base_score * 1.25
                game.score += int(self.base_score)
            elif game.level < 10:
                game.lives += 15
                self.base_score = self.base_score * 1.50
                game.score += int(self.base_score)
            elif game.level < 15:
                game.lives += 20
                self.base_score = self.base_score * 1.75
                game.score += int(self.base_score)
            else:
                game.lives += 50
                self.base_score = self.base_score * 3.5
                game.score *= int(self.base_score)
        elif game.difficulty == 'Medium':
            if game.level < 5:
                game.lives += 5
                self.base_score = self.base_score * 1.50
                game.score += int(self.base_score)
            elif game.level < 10:
                game.lives += 10
                self.base_score = self.base_score * 2
                game.score += int(self.base_score)
            elif game.level < 15:
                game.lives += 15
                self.base_score = self.base_score * 2.5
                game.score += int(self.base_score)
            else:
                game.lives += 35
                self.base_score = self.base_score * 10
                game.score *= int(self.base_score)
        else:
            if game.level < 5:
                self.base_score = self.base_score * 2
                game.score += int(self.base_score)
            elif game.level < 10:
                game.lives += 5
                self.base_score = self.base_score * 3
                game.score += int(self.base_score)
            elif game.level < 15:
                game.lives += 10
                self.base_score = self.base_score * 4
                game.score += int(self.base_score)
            else:
                game.lives += 25
                self.base_score = self.base_score * 20
                game.score *= int(self.base_score)

        # Creates scientific notation if score exceeds 6 figures
        if game.score > 999999:
            game.score = "{:.2e}".format(game.score)

        game.level += 1
        


    def generate(self):
        # Meeshko kidnaps a new number
        self.label_to.text = str(int(self.label_to.text) * 2)
        temp = random.randint(0, int(self.label_to.text))
        if game.curr == temp: self.generate()
        else: game.curr = temp


    def update(self):
        # Updates score and lives labels
        self.label_score.text = str(game.score)
        self.label_lives.text = str(game.lives)
        self.label_level.text = str(game.level)

        # Prevents update if hint is present
        if self.label_input.text in ['HIGHER', 'LOWER']:
            pass
        else: self.label_input.text = ''

        
    def delete(self):
        if self.label_input.text != '':
            self.label_input.text = self.label_input.text[:-1]
        

    def submit(self):
        print(game.curr)

        if self.check_input():
            pass
        else:
            # Checks if the guess is correct and calls score() function
            if int(self.label_input.text) == game.curr:
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
