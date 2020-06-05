# -*- coding: utf-8 -*-
"""
Created on Wed May 27 14:57:39 2020

@author: harsh
"""


import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup

class P(FloatLayout):
    pass

class Widgets(Widget):
    def btn(self):
        show_popup()
        

class PopApp(App):
	def build(self):
		return Widgets()

def show_popup():
    show= P()
    popupWindow = Popup(title ="Popup Window",content =show,size_hint=(None,None),size=(400,400))
    popupWindow.open()

if __name__=="__main__":
	PopApp().run()