from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class Game():
    def __init__(self, difficulty='Medium', start_gold='1000') -> None:
        self.difficulty = difficulty
        self.start_gold = start_gold


    def printr(self):
        print(self.difficulty)
        print(self.start_gold)


game = Game()


class MainMenu(Widget):
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


class MeeshkosNumberApp(App):
    def build(self):
        return MainMenu()


if __name__ == '__main__':
    MeeshkosNumberApp().run()
