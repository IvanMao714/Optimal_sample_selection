from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout

from algorithms.offical_edition import search
from database import database
from database.database import Database


class DownloadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    cwdir = ObjectProperty(None)


class SelectDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    input = ObjectProperty(None)
    config = ObjectProperty(None)

    def run_algorithms(self):
        self.config.result = search(self.config.m, self.config.n, self.config.k, self.config.j, self.config.s)
        return self.config.result

    def import_database(self):
        input_format = str(self.config.m) + "-" + str(self.config.n) + "-" + \
                       str(self.config.k) + "-" + str(self.config.j) + "-" + str(self.config.s)
        database = Database()
        database.insert_one(input_format, self.config.result)
        return "Upload Successfully!!!!"


Factory.register("SelectDialog", cls=SelectDialog)
Factory.register("DownloadDialog", cls=DownloadDialog)
