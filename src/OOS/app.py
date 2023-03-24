"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


import toga
from toga.style.pack import COLUMN, LEFT, RIGHT, ROW, Pack



class OptimalSampleSelection(toga.App):

    # def startup(self):
    #     main_box = toga.Box()

    #     self.main_window = toga.MainWindow(title=self.formal_name)
    #     self.main_window.content = main_box
    #     self.main_window.show()

    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        m_value = toga.Label(
            "The values for parameters m: ",
            style=Pack(padding=(0, 10))
        )
        self.m_input = toga.TextInput(style=Pack(flex=10))

        n_value = toga.Label(
            "The values for parameters n: ",
            style=Pack(padding=(0, 5))
        )
        self.n_input = toga.TextInput(style=Pack(flex=1))

        k_value = toga.Label(
            "The values for parameters k: ",
            style=Pack(padding=(0, 10))
        )
        self.k_input = toga.TextInput(style=Pack(flex=10))

        j_value = toga.Label(
            "The values for parameters j: ",
            style=Pack(padding=(0, 5))
        )
        self.j_input = toga.TextInput(style=Pack(flex=1))

        s_value = toga.Label(
            "The values for parameters s: ",
            style=Pack(padding=(0, 5))
        )
        self.s_input = toga.TextInput(style=Pack(flex=1))

        # name_label = toga.Label(
        #     "Your name: ",
        #     style=Pack(padding=(0, 5))
        # )
        # self.name_input = toga.TextInput(style=Pack(flex=1))

        name_box = toga.Box(style=Pack(direction=COLUMN, padding=10))
        name_box.add(m_value)
        name_box.add(self.m_input)
        name_box.add(n_value)
        name_box.add(self.n_input)
        name_box.add(k_value)
        name_box.add(self.k_input)
        name_box.add(j_value)
        name_box.add(self.j_input)
        name_box.add(s_value)
        name_box.add(self.s_input)


        button = toga.Button(
            "Say Hello!",
            on_press=self.say_hello,
            style=Pack(padding=5)
        )

        main_box.add(name_box)
        main_box.add(button)

        self.main_window = toga.MainWindow(title="An Optimal Sample Selection System")
        self.main_window.content = main_box
        self.main_window.show()

    def say_hello(self, widget):
        print(f"Hello, {self.m_input.value}")




def main():
    return OptimalSampleSelection()
