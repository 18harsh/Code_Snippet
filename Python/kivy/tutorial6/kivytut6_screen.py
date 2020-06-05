# -*- coding: utf-8 -*-
"""
Created on Wed May 27 13:31:01 2020

@author: harsh
"""


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen

class MainWindow(Screen):
    pass
class SecondWindow(Screen):
    pass
class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("myapp.kv")


class MyMainApp(App):
	def build(self):
		return kv


if __name__=="__main__":
	MyMainApp().run()