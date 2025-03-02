import pygame
import math

background_colour = (255,255,255)
(width, height) = (1200, 800)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simulation')
screen.fill(background_colour)
black = (0,0,0)

#MAIN BOX DEFINITION
box = pygame.Rect(400,200,400,400)
boxBorderLeft = box.left
boxBorderTop = box.top
boxBorderBot = box.bottom
boxBorderRight = box.right

running = True
while running:

  pygame.display.flip()
  screen.fill(background_colour)
  pygame.draw.rect(screen,black,box,1)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

