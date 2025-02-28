import pygame
import random 
import math 

background_colour = (255,255,255)
(width, height) = (1200, 800)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simulation')
screen.fill(background_colour)

class Particle:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.colour = (0, 0, 255)
        self.thickness = 1

    def display(self):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size, self.thickness)

    def move(self):
        self.x += 1
        self.y += 1

    def moveTowardMouse(self,x,y):
       direction = self.findDir(x,y)
       self.x += direction[0]
       self.y += direction[1]
       
    def update(self):
       self.display()
       position = pygame.mouse.get_pos()
       self.moveTowardMouse(position[0],position[1])

    def findDir(self,x,y):
       delta_x = x - self.x
       delta_y = y - self.y

       return (1/50 * delta_x, 1/50 * delta_y)
       
def refresh_screen(particle):
   pygame.display.flip()
   screen.fill(background_colour)
   particle.update()

first_particle = Particle(100,100,10)

running = True

while running:
  refresh_screen(first_particle)

  position = pygame.mouse.get_pos()
  print(f"The position of the mouse is -> {position}")

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

