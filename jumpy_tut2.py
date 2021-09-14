#import libraries
import pygame

#initialise pygame
pygame.init()

#game window dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Jumpy')

#define colours
WHITE = (255, 255, 255)

#load images
jumpy_image = pygame.image.load('assets/jump.png').convert_alpha()
bg_image = pygame.image.load('assets/bg.png').convert_alpha()


#player class
class Player():
	def __init__(self, x, y):
		self.image = pygame.transform.scale(jumpy_image, (45, 45))
		self.width = 25
		self.height = 40
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = (x, y)

	def draw(self):
		screen.blit(self.image, (self.rect.x - 12, self.rect.y - 5))
		pygame.draw.rect(screen, WHITE, self.rect, 2)


jumpy = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)

#game loop
run = True
while run:

	#draw background
	screen.blit(bg_image, (0, 0))

	#draw sprites
	jumpy.draw()


	#event handler
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False


	#update display window
	pygame.display.update()



pygame.quit()

