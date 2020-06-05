import pygame
from pygame.locals import *
import math
import random

pygame.init()

WIDTH = 900
HEIGHT = 400

bg =  pygame.transform.scale(pygame.image.load('images/background.jpg'),(WIDTH,HEIGHT))
ball_img = pygame.transform.scale(pygame.image.load('images/ball.png'),(40,40))

win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("BasketBall")


class ball (object):
	def __init__(self,x,y,radius,color):
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color

	def draw(self,win):
		win.blit(ball_img,(self.x,self.y))
		# pygame.draw.circle(win,(0,0,0),(self.x,self.y),self.radius)
		# pygame.draw.circle(win,self.color,(self.x,self.y),self.radius-1)	

	@staticmethod
	def ballPath(startx,starty,power,ang,time):
		velx = math.cos(angle)*power
		vely = math.sin(angle)*power
		distx = velx*time
		disty = (vely *time)+((-4.9 * (time)**2)/2)

		newx = round(distx + startx)
		newy = round(starty - disty)

		return (newx,newy)

def redrawwindow():
	win.blit(bg, (0,0))
	
	basketball.draw(win)
	

def drawline():
	pass

def find_angle(initial,last):
	try:
		return math.atan((last[1]-initial[1])/(last[0]-initial[0]))
	except:
		pass	


x = random.randint(200,700)
y =	random.randint(30,250)


basketball = ball(x,y,40,(255,255,255))
aim = False
run = True
time = 0
shoot = False
while run:
	redrawwindow()
	if shoot:
		if basketball.y<HEIGHT - basketball.radius:
			time+=0.03
			po = ball.ballPath(x,y,speed,angle,time)
			basketball.x = po[0]
			basketball.y = po[1]
		else:
			shoot = False
			basketball.y = HEIGHT - basketball.radius

	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if 	event.type == pygame.MOUSEBUTTONDOWN:
				print("aim")
				aim = True
				initial_pos = pygame.mouse.get_pos()
				current_pos = initial_pos
			if	event.type == pygame.MOUSEBUTTONUP:
				print("shoot")
				aim = False
				shoot = True
				last_pos = pygame.mouse.get_pos()
				line_dist = math.sqrt((last_pos[0]-initial_pos[0])**2+(last_pos[1]-initial_pos[1])**2)
				speed = (line_dist/8)
				angle = find_angle(initial_pos,last_pos)
				print("speed",speed,"angle:",angle)
				
				
			if event.type == pygame.MOUSEMOTION:
				if aim:
					print("aiming")
					current_pos = pygame.mouse.get_pos()

	if aim:
		pygame.draw.line(win,(255,255,255),initial_pos,current_pos)

	


	pygame.display.update()

pygame.quit()