from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from timecontrol import FocusTimer, LazyTimer

class PomodoroPy(App):

    def build(self):
        ftimer = FocusTimer()
        ltimer = LazyTimer()

        grid = GridLayout(cols=2)
        box = BoxLayout(orientation='vertical')

        button_f = Button(text="Foco", size_hint=(1, .3), on_press=self.start_count)
        button_l = Button(text="Descanso", size_hint=(1, .3))
        title = Label(text="PomodoroPy", size_hint=(1, .2))

        self.label_f = Label(text=str(ftimer.focus_time))
        self.label_l = Label(text=str(ltimer.lazy_time))

        box.add_widget(title)
        grid.add_widget(button_f)
        grid.add_widget(button_l)
        grid.add_widget(self.label_f)
        grid.add_widget(self.label_l)
        box.add_widget(grid)

        return box

    def start_count(self, button):
        print("Botão apertado")
        self.label_f.text = str(int(self.label_f.text) - 1)

PomodoroPy().run()

