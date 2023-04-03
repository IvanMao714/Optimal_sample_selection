"""
My first application
"""
import toga
from toga.style.pack import COLUMN, LEFT, RIGHT, ROW, Pack, CENTER


class OptimalSampleSelection(toga.App):

    # def startup(self):
    #     main_box = toga.Box()

    #     self.main_window = toga.MainWindow(title=self.formal_name)
    #     self.main_window.content = main_box
    #     self.main_window.show()

    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        hp_box = toga.Box(style=Pack(direction=COLUMN))

        m_box = toga.Box(style=Pack(padding_top=20, padding_right=20, padding_left=10, direction=ROW))
        m_value = toga.Label(
            "The values for parameters m (45<= m <=54): ",
            style=Pack(font_family="cursive",font_weight="bold")
        )
        self.m_input = toga.TextInput(style=Pack(flex=10, width=300))

        n_box = toga.Box(style=Pack(padding_top=20, padding_right=20, padding_left=10))
        n_value = toga.Label(
            "The values for parameters n (7<= n <=25):   ",
            style=Pack(font_family="cursive",font_weight="bold")
        )
        self.n_input = toga.TextInput(style=Pack(flex=10, width=300))

        k_box = toga.Box(style=Pack(padding_top=20, padding_right=20, padding_left=10))
        k_value = toga.Label(
            "The values for parameters k (4<= k <=7):     ",
            style=Pack(font_family="cursive",font_weight="bold")
        )
        self.k_input = toga.TextInput(style=Pack(flex=10, width=300))

        j_box = toga.Box(style=Pack(padding_top=20, padding_right=20, padding_left=10))
        j_value = toga.Label(
            "The values for parameters j (s<= j <=k):      ",
            style=Pack(font_family="cursive",font_weight="bold")
        )
        self.j_input = toga.TextInput(style=Pack(flex=10, width=300))

        s_box = toga.Box(style=Pack(padding_top=20, padding_right=20, padding_left=10,padding_bottom=20))
        s_value = toga.Label(
            "The values for parameters j (3<= s <=7):     ",
            style=Pack(font_family="cursive",font_weight="bold")
        )
        self.s_input = toga.TextInput(style=Pack(flex=10, width=300))

        output = toga.MultilineTextInput(style=Pack(padding_top=20, padding_right=10, padding_left=10,height=150))

        m_box.add(m_value)
        m_box.add(self.m_input)

        n_box.add(n_value)
        n_box.add(self.n_input)

        k_box.add(k_value)
        k_box.add(self.k_input)

        j_box.add(j_value)
        j_box.add(self.j_input)

        s_box.add(s_value)
        s_box.add(self.s_input)

        button_box = toga.Box(style=Pack(direction=ROW))

        button_rs = toga.Button(
            "Random Selection",
            on_press=self.say_hello,
            style=Pack(padding=5,flex=100)
        )

        button_ss = toga.Button(
            "Specified Selection",
            on_press=self.say_hello,
            style=Pack(padding=5,flex=100)
        )

        button_box.add(button_rs)
        button_box.add(button_ss)

        # divider1 = toga.Divider()
        # divider2 = toga.Divider()

        # main_box.add(divider1)
        main_box.add(m_box)
        main_box.add(n_box)
        main_box.add(k_box)
        main_box.add(j_box)
        main_box.add(s_box)
        main_box.add(button_box)
        # main_box.add(divider2)
        main_box.add(output)

        # main_box.add(divider)

        self.main_window = toga.MainWindow(title="An Optimal Sample Selection System",)
        self.main_window.content = main_box
        self.main_window.show()

    def say_hello(self, widget):
        print(f"Hello, {self.m_input.value}")


def main():
    return OptimalSampleSelection()
