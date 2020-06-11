from random import *
from turtle import *

from base import vector

ball = vector(-200,-200)
speed = vector(0,0)
target = []

def inside(xy):
	return -200<xy.x <200 and -200 <xy.y<200

def tap(x,y):
	if not inside(ball):
		ball.x = 199
		ball.y = 199
		speed.x = (x+200)/25
		speed.y = (y+200)/25

def draw():
	clear()
	for target in targets:
		goto(target.x,target.y)
		dot(20,'blue')
	if inside(ball):
		goto(ball.x,ball.y)
		dot(6,'red')	

def move():
	if randrange(40) == 0:
		y = randrange(-150,150)
		target = vector(200,y)
		
setup(420,420,370,0)