import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Grid(GridLayout):
    def pressed(self, instance):
        print('pressed')

    def __init__(self, **kwargs):
        super(Grid, self).__init__(**kwargs)
        self.cols = 1

        self.add_widget(Label(text="Mishko's Number", font_size=75))

        self.start_params = GridLayout()
        self.start_params.cols = 2
        self.start_params.add_widget(Label(text='From:', font_size=25))
        self.ifrom = TextInput(multiline=False)
        self.start_params.add_widget(self.ifrom)
        self.start_params.add_widget(Label(text='To:', font_size=25))
        self.ito = TextInput(multiline=False)
        self.start_params.add_widget(self.ito)

        self.start_game = GridLayout()
        self.start_game.cols = 2
      
        self.difficulty_buttons = GridLayout()
        self.difficulty_buttons.cols = 3

        self.easy = Button(text='Easy', font_size=25)
        self.easy.bind(on_press=self.pressed)
        self.difficulty_buttons.add_widget(self.easy)
        self.med = Button(text='Medium', font_size=25)
        self.med.bind(on_press=self.pressed)
        self.difficulty_buttons.add_widget(self.med)
        self.hard = Button(text='Hard', font_size=25)
        self.hard.bind(on_press=self.pressed)
        self.difficulty_buttons.add_widget(self.hard)

        self.start_game.add_widget(Label(text='Difficulty:', font_size=25))

        self.start_game.add_widget(self.difficulty_buttons)

        self.submit = Button(text='Submit', font_size=25)
        self.submit.bind(on_press=self.pressed)
        self.start_game.add_widget(self.submit)

        self.add_widget(self.start_params)
        self.add_widget(self.start_game)

class MishkosNumberApp(App):
    def build(self):
        return Grid()

if __name__ == '__main__':
    MishkosNumberApp().run()