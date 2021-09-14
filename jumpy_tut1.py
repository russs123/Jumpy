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

#load images
bg_image = pygame.image.load('assets/bg.png').convert_alpha()



#game loop
run = True
while run:

	#draw background
	screen.blit(bg_image, (0, 0))



	#event handler
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False


	#update display window
	pygame.display.update()



pygame.quit()

