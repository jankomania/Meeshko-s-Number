import time
import datetime
import random
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class Game():
    def __init__(self, difficulty='Medium', start_gold='1000') -> None:
        self.difficulty = difficulty
        self.start_gold = start_gold


    def printr(self):
        print(self.difficulty)
        print(self.start_gold)


game = Game()


class MainMenu(GridLayout):
    def easy(self, instance):
        game.difficulty = 'Easy'
        game.start_gold = '500'

    def med(self, instance):
        game.difficulty = 'Medium'
        game.start_gold = '1000'

    def hard(self, instance):
        game.difficulty = 'Hard'
        game.start_gold = '1500'

    def printr(self, instance):
        game.printr()


    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)

        self.button_easy = Button(text='Easy', font_size=25)
        self.button_easy.bind(on_press=self.easy)

        self.button_med = Button(text='Medium', font_size=25)
        self.button_med.bind(on_press=self.med)

        self.button_hard = Button(text='Hard', font_size=25)
        self.button_hard.bind(on_press=self.hard)


        # Difficulty buttons Grid
        self.difficulty_buttons = GridLayout()
        self.difficulty_buttons.cols = 3

        self.difficulty_buttons.add_widget(self.button_easy)
        self.difficulty_buttons.add_widget(self.button_med)
        self.difficulty_buttons.add_widget(self.button_hard)


        # Difficulty Grid
        self.difficulty = GridLayout()
        self.difficulty.cols = 2
        self.difficulty.add_widget(Label(text='Difficulty:', font_size=25))
        self.difficulty.add_widget(self.difficulty_buttons)


        # Final Grid
        self.final = GridLayout()
        self.final.cols = 1
        
        # Submit Button
        self.submit = Button(text='START GAME', font_size=50)
        self.submit.bind(on_press=self.printr)

        self.final.add_widget(self.difficulty)
        self.final.add_widget(self.submit)

         # Main Grid
        self.cols = 1
        
        self.add_widget(Label(text="Mishko's Number", font_size=75))

        self.add_widget(self.final)

class Grid(GridLayout):
    def __init__(self, **kwargs):
        super(Grid, self).__init__(**kwargs)
        self.cols = 1

        self.add_widget(Label(text='SUCCESS', font_size=100))

def countdown():
    total_seconds = 5
    while total_seconds > 0:
 
        # Timer represents time left on countdown
        timer = datetime.timedelta(seconds = total_seconds)
        
        # Prints the time left on the timer
        print(timer, end="\r")
 
        # Delays the program one second
        time.sleep(1)
 
        # Reduces total time by one second
        total_seconds -= 1
 
    return bool(random.getrandbits(1))


class MishkosNumberApp(App):
    def build(self):
        return Grid()


if __name__ == '__main__':
    MishkosNumberApp().run()
