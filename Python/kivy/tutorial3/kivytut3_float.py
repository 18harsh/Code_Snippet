# -*- coding: utf-8 -*-
"""
Created on Tue May 26 23:10:40 2020

@author: harsh
"""

import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class FltApp(App):
	def build(self):
		return FloatLayout()
    

if __name__=="__main__":
	FltApp().run()
