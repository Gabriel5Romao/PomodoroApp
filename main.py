from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from timecontrol import FocusTimer, LazyTimer

class PomodoroPy(App):

    def build(self):
        # Classes to manage the time
        ftimer = FocusTimer()
        ltimer = LazyTimer()

        # Minimal Layout
        grid = GridLayout(cols=2)
        box = BoxLayout(orientation='vertical')
        button_f = Button(text="Foco", size_hint=(1, .3), on_press=self._)
        button_l = Button(text="Descanso", size_hint=(1, .3))
        title = Label(text="PomodoroPy", size_hint=(1, .2))

        # Adjusting the timer's label
        self.label_f = Label(text="{} : {}".format(self.convert_time(ftimer.focus_time)[0], self.convert_time(ftimer.focus_time)[1]))
        self.label_l = Label(text="{} : {}".format(self.convert_time(ltimer.lazy_time)[0], self.convert_time(ltimer.lazy_time)[1]))

        box.add_widget(title)
        grid.add_widget(button_f)
        grid.add_widget(button_l)
        grid.add_widget(self.label_f)
        grid.add_widget(self.label_l)
        box.add_widget(grid)

        return box

    def _(self, button):
        if button.state == 'down':
            Clock.schedule_interval(self.reduce_time, 1)

    # Functions to work the time
    def convert_time(self, timestr):
        minutes = int(timestr) // 60
        seconds = int(timestr) % 60
        return (minutes, seconds)

    def reconvert_time(self, time):
        tm = int(time.split(':')[0]) * 60
        ts = int(time.split(':')[1])
        return tm + ts

    def reduce_time(self, _):
        reduced_time = str(self.reconvert_time(self.label_f.text) - 1)
        self.label_f.text = f"{self.convert_time(reduced_time)[0]} : {self.convert_time(reduced_time)[1]}"

PomodoroPy().run()

