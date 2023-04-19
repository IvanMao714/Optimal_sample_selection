from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class SelectPage(FloatLayout):

    def __init__(self, config, **kwargs):
        super().__init__(**kwargs)
        self.config = config

    @staticmethod
    def page_index(*args):
        App.get_running_app().screen_manager.current = "Index_page"
        App.get_running_app().screen_manager.transition.direction = 'right'
