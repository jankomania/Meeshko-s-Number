import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Game():
    def __init__(self, difficulty='Medium') -> None:
        self.difficulty = difficulty
        self.start_gold = self.gold(self.difficulty)

    # Sets the starting gold according to the selected difficulty (default 'Medium')
    def gold(self, difficulty):
        if difficulty == 'Easy':
            return 1500
        if difficulty == 'Medium':
            return 1000
        if difficulty == 'Hard':
            return 500

    def printr(self):
        print(self.difficulty)
        print(self.start_gold)


game = Game()


class Grid(GridLayout):
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
        super(Grid, self).__init__(**kwargs)
        self.cols = 1

        # Main Grid
        self.add_widget(Label(text="Mishko's Number", font_size=75))


        # Start Parameters Grid 
        self.start_params = GridLayout()
        self.start_params.cols = 2
        
        self.start_params.add_widget(Label(text='From:', font_size=25))
        self.ifrom = TextInput(multiline=False)
        self.start_params.add_widget(self.ifrom)

        self.start_params.add_widget(Label(text='To:', font_size=25))
        self.ito = TextInput(multiline=False)
        self.start_params.add_widget(self.ito)


        # Difficulty Grid
        self.start_game = GridLayout()
        self.start_game.cols = 2
      
        self.difficulty_buttons = GridLayout()
        self.difficulty_buttons.cols = 3

        self.button_easy = Button(text='Easy', font_size=25)
        self.button_easy.bind(on_press=self.easy)
        self.difficulty_buttons.add_widget(self.button_easy)

        self.button_med = Button(text='Medium', font_size=25)
        self.button_med.bind(on_press=self.med)
        self.difficulty_buttons.add_widget(self.button_med)

        self.button_hard = Button(text='Hard', font_size=25)
        self.button_hard.bind(on_press=self.hard)
        self.difficulty_buttons.add_widget(self.button_hard)

        self.start_game.add_widget(Label(text='Difficulty:', font_size=25))

        self.start_game.add_widget(self.difficulty_buttons)


        # Submit Button
        self.submit = Button(text='Submit', font_size=25)
        self.submit.bind(on_press=self.printr)
        self.add_widget(self.submit)

        
        # Adds the Start Parameters and Start Game Grid to Final Grid and then to the Main Grid
        self.final = GridLayout()
        self.final.cols = 1

        self.final.add_widget(self.start_params)
        self.final.add_widget(self.start_game)

        self.add_widget(self.final)



class MishkosNumberApp(App):
    def build(self):
        return Grid()


if __name__ == '__main__':
    MishkosNumberApp().run()
