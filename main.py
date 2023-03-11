import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from random import randint


kivy.require('2.1.0')

class MyRoot(BoxLayout):
    def __init__(self):
        super(MyRoot, self).__init__()
    def generate_number(self):
        self.random_label.text = str(randint(0,1000))

class NeuralRandom(App):
    def build(self):
        return MyRoot()

aplicativo = NeuralRandom()
aplicativo.run()