# -*- coding: utf-8 -*-
"""
Created on Wed May 27 16:29:26 2020

@author: harsh
"""

import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase


class WindowManager(ScreenManager):
	pass


class LoginWindow(Screen):
	email = ObjectProperty(None)
	password = ObjectProperty(None)

	def loginBtn(self):
		if db.validate(self.email.text,self.password.text):
			MainWindow.current = self.email.text
			self.reset()
			sm.current = "main"
		else:
			self.reset()
			invalidLogin()

	def createBtn(self):
		self.reset()
		sm.current = "create"

	def reset(self):
		self.email.text = ""
		self.password.text = ""

class MainWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    current = ""

    def logOut(self):
        sm.current = "login"

    def on_enter(self, *args):
        password, name, created = db.get_user(self.current)
        self.n.text = "Account Name: " + name
        self.email.text = "Email: " + self.current
        self.created.text = "Created On: " + created



class CreateAccountWindow(Screen):
	namee = ObjectProperty(None)
	email = ObjectProperty(None)
	password = ObjectProperty(None)

	def submit(self):
		if self.namee.text!="" and self.email.text!="" and self.email.text.count("@") == 1 and self.email.text.count(".")>0:
			if self.password.text != "":
				if db.add_user(self.email.text,self.password.text,self.namee.text) == 1:
					self.reset()
					sm.current="login"
				else:
					invalidEmail()
			else:
				invalidForm()
		else:
			invalidForm()		

	def login(self):
		self.reset()
		sm.current = "login"

	def reset(self):
		self.email.text = ""
		self.password.text = ""
		self.namee.text = ""

def invalidLogin():
	pop = Popup(title="Invalid Login",
				content = Label(text='Invalid username or password.'),
				size_hint=(None,None),size=(400, 400))
	pop.open()

def invalidForm():
	pop = Popup(title="Invalid Form",
				content = Label(text='Please fill in all inputs with valid information.'),
				size_hint=(None,None),size=(400, 400))
	pop.open()

def invalidEmail():
	pop = Popup(title="Invalid Email",
				content = Label(text='Email already exist.'),
				size_hint=(None,None),size=(400, 400))
	pop.open()	


kv = Builder.load_file("gui.kv")
sm = WindowManager()
db = DataBase("users.txt")

screens = [LoginWindow(name = "login"),CreateAccountWindow(name="create"),MainWindow(name="main")]
for screen in screens:
	sm.add_widget(screen)

sm.current = "login"


class MyMainApp(App):
	def build(self):
		return sm

if __name__=="__main__":
	MyMainApp().run()