import pygame
import button

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1378

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Button Demo')

start_img = pygame.image.load('start_btn.png').convert_alpha()
exit_img = pygame.image.load('exit_btn.png').convert_alpha()

start_button = button.Button(100, 200, start_img, 0.8)
exit_button = button.Button(450, 200, exit_img, 0.8)

run = True
while run:

	screen.fill((202, 228, 241))

	if start_button.draw(screen):
		ok=True
		run=False
	if exit_button.draw(screen):
		run=False

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()
