from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class Programa(App):

    def build(self):

        box = BoxLayout()
        self.label = Label(text="1")
        button = Button(text="Aperte", on_press=self.incrementa)

        box.add_widget(button)
        box.add_widget(self.label)

        return box

    def incrementa(self, button):
        print(self)
        print(button)
        print(button.state)
        print(type(button.state))
        self.label.text = str(int(self.label.text) + 1)
        



Programa().run()