import random

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup

from Dialog import SelectDialog

from algorithms.offical_edition import search


class SelectPage(FloatLayout):

    def __init__(self, config, **kwargs):
        super().__init__(**kwargs)
        self.config = config

    @staticmethod
    def page_index(*args):
        App.get_running_app().screen_manager.current = "Index_page"
        App.get_running_app().screen_manager.transition.direction = 'right'

    @staticmethod
    def page_database(*args):
        App.get_running_app().screen_manager.current = "Database_page"
        App.get_running_app().screen_manager.transition.direction = 'left'

    def random_select(self):
        self.config.m = random.randint(45, 54)
        self.config.n = random.randint(7, 10)
        self.config.k = random.randint(4, 7)
        self.config.s = random.randint(3, self.config.k)
        self.config.j = random.randint(self.config.s, self.config.k)
        self.selectdialog_load(self.config.m, self.config.n, self.config.k, self.config.j, self.config.s)

        # content.ids.result.text = self.config.result

    def selectdialog_load(self, m, n, k, j, s):
        input = "The input is: m = " + str(m) + ", n = " + str(n) + ", k = " + str(k) + \
                ", j = " + str(j) + ", s = " + str(s) + ", The result is:"
        content = SelectDialog(load=self.import_database, cancel=self.dismiss_popup, input=input, config=self.config)
        self._popup = Popup(title="Run Algorithms Setting", content=content, size_hint=(.9, .9))
        self._popup.open()

    def import_database(self):
        self.dismiss_popup()

    def dismiss_popup(self):
        self._popup.dismiss()

