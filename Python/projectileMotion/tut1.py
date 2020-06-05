import pygame
import math

width = 1200
height = 500

win = pygame.display.set_mode((width,height))

class ball (object):
	def __init__(self,x,y,radius,color):
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color
	def draw(self,win):
		pygame.draw.circle(win,(0,0,0),(self.x,self.y),self.radius)
		pygame.draw.circle(win,self.color,(self.x,self.y),self.radius-1)

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
	win.fill((64,64,64))
	golfball.draw(win)
	pygame.draw.line(win,(255,255,255),line[0],line[1])
	pygame.display.update()

def findAngle(pos):
	sx = golfball.x
	sy = golfball.y
	try:
		angle = math.atan((sy - pos[1])/(sx - pos[0]))
	except:
		angle = math.pi/2
	if pos[1] < sy and pos[0] > sx:
		angle = abs(angle)
	elif pos[1] < sy and pos[0] <sx:
		angle = math.pi -angle
	elif pos[1] > sy and pos[0]>sx:
		angle = math.pi + abs(angle)
	elif pos[1] > sy and pos[0]>sx:
		angle = (math.pi*2)-angle
	return angle					


golfball = ball(300,494,5,(255,255,255))
x = 0
y = 0
time = 0
power = 0
angle = 0
shoot = False

run = True
while run:
	if shoot:
		if golfball.y<500 - golfball.radius:
			time+=0.03
			po = ball.ballPath(x,y,power,angle,time)
			golfball.x = po[0]
			golfball.y = po[1]
		else:
			shoot = False
			golfball.y = 494	
	pos = pygame.mouse.get_pos()
	line = [(golfball.x,golfball.y),pos]
	redrawwindow()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if 	event.type == pygame.MOUSEBUTTONDOWN:
			if shoot == False:
				shoot = True
				x = golfball.x
				y = golfball.y
				time = 0
				power = math.sqrt((line[1][1]- line[0][1])**2+(line[1][0]-line[0][0])**2)/8
				angle = findAngle(pos)

pygame.quit()			