from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout


class DownloadDialog(FloatLayout):
    '''
    弹窗的加载和取消属性定义
    '''
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    cwdir = ObjectProperty(None)

Factory.register("DownloadDialog", cls=DownloadDialog)