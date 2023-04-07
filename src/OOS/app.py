"""
My first application
"""
import toga
from toga.style.pack import COLUMN, ROW, Pack
from . import algorithms


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
            style=Pack(font_family="cursive", font_weight="bold")
        )
        self.m_input = toga.TextInput(style=Pack(flex=10, width=300))

        n_box = toga.Box(style=Pack(padding_top=20, padding_right=20, padding_left=10))
        n_value = toga.Label(
            "The values for parameters n (7<= n <=25):   ",
            style=Pack(font_family="cursive", font_weight="bold")
        )
        self.n_input = toga.TextInput(style=Pack(flex=10, width=300))

        k_box = toga.Box(style=Pack(padding_top=20, padding_right=20, padding_left=10))
        k_value = toga.Label(
            "The values for parameters k (4<= k <=7):     ",
            style=Pack(font_family="cursive", font_weight="bold")
        )
        self.k_input = toga.TextInput(style=Pack(flex=10, width=300))

        j_box = toga.Box(style=Pack(padding_top=20, padding_right=20, padding_left=10))
        j_value = toga.Label(
            "The values for parameters j (s<= j <=k):      ",
            style=Pack(font_family="cursive", font_weight="bold")
        )
        self.j_input = toga.TextInput(style=Pack(flex=10, width=300))

        s_box = toga.Box(style=Pack(padding_top=20, padding_right=20, padding_left=10, padding_bottom=20))
        s_value = toga.Label(
            "The values for parameters j (3<= s <=7):     ",
            style=Pack(font_family="cursive", font_weight="bold")
        )
        self.s_input = toga.TextInput(style=Pack(flex=10, width=300))

        output = toga.MultilineTextInput(style=Pack(padding_top=20, padding_right=10, padding_left=10, height=150),
                                         readonly=True)

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
            on_press=self.random_selection,
            style=Pack(padding=5, flex=100)
        )

        button_ss = toga.Button(
            "Specified Selection",
            on_press=self.random_selection,
            style=Pack(padding=5, flex=100)
        )

        button_box.add(button_rs)
        button_box.add(button_ss)

        homepage = toga.Box(style=Pack(direction=COLUMN))
        homepage.add(m_box)
        homepage.add(n_box)
        homepage.add(k_box)
        homepage.add(j_box)
        homepage.add(s_box)
        homepage.add(button_box)
        homepage.add(output)

        container = toga.OptionContainer()

        container.add('Homepage', homepage)
        # container.add('Database', homepage)

        main_box.add(container)

        # main_box.add(divider)

        self.main_window = toga.MainWindow(title="An Optimal Sample Selection System", )
        self.main_window.content = main_box
        self.main_window.show()

    def random_selection(self,widget):
        m = int(self.m_input.value)
        n = int(self.n_input.value)
        k = int(self.k_input.value)
        j = int(self.j_input.value)
        s = int(self.s_input.value)
        # results = "111"
        results = algorithms.search(m, n, k, j, s)
        # print(results)
        self.output.value = str(results)


def main():
    return OptimalSampleSelection()
