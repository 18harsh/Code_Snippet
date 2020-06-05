import pygame
from network import Network

pygame.init()

class Player():
	width = height = 50

	def __init__(self, startx, starty, color=(255,0,0)):
		self.x = startx
		self.y = starty
		self.velocity = 2
		self.color = color

	def draw(self, g):
		pygame.draw.rect(g, self.color ,(self.x, self.y, self.width, self.height), 0)

	def move(self, dirn):
		if dirn == 0:
			self.x += self.velocity
		elif dirn == 1:
			self.x -= self.velocity
		elif dirn == 2:
			self.y -= self.velocity
		else:
			self.y += self.velocity

class Game:
	def __init__(self,w,h):
		self.net = Network()
		self.width = w
		self.height = h
		self.player1 = Player(50,50)
		self.player2 = Player(100,100)
		self.canvas = Canvas(self.width,self.height,"Testing...")

	def run(self):
		clock = pygame.time.Clock()
		run = True
		while run:
			clock.tick(60)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
				if event.type == pygame.K_ESCAPE:
					run = False

			keys = pygame.key.get_pressed()

			if keys[pygame.K_RIGHT]:
				if self.player1.x <= self.width - self.player1.velocity:
					self.player1.move(0)
			
			if keys[pygame.K_LEFT]:
				if self.player1.x >= self.player1.velocity:
					self.player1.move(1)

			if keys[pygame.K_UP]:
				if self.player1.y >= self.player1.velocity:
					self.player1.move(2)

			if keys[pygame.K_DOWN]:
				if self.player1.y <= self.height - self.player1.velocity:
					self.player1.move(3)
			
			self.player2.x,self.player2.y = self.parse_data(self.send_data())

			self.canvas.draw_background()
			self.player1.draw(self.canvas.get_canvas())
			self.player2.draw(self.canvas.get_canvas())
			self.canvas.update()

		pygame.quit()

	def send_data(self):
		data = str(self.net.id) + ":" + str(self.player1.x) + "," + str(self.player1.y)
		reply = self.net.send(data)
		return reply

	@staticmethod
	def parse_data(data):
		try:
			d = data.split(":")[1].split(",")
			return int(d[0]), int(d[1])
		except:
			return 0,0

class Canvas:
	def __init__(self,w,h,name="None"):
		self.width = w
		self.height = h
		self.win = pygame.display.set_mode((self.width,self.height))
		pygame.display.set_caption(name)

	@staticmethod
	def update():
		pygame.display.update()

	def draw_text(self,text,size,x,y):
		font = pygame.font.SysFont("comicsans", size)
		render = font.render(text, 1, (0,0,0))
		self.screen.draw(render, (x,y))

	def get_canvas(self):
		return self.win

	def draw_background(self):
		self.win.fill((255,255,255))	    