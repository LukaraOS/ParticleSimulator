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

    def findDir(self,a,b):
       """Find direction towards the point pos
        returns the polar coordonates (p,q) towards that point"""
       distA = a-self.x
       distB = math.sqrt((b+self.y)**2+(a+self.y)**2)
       angle = math.acos(distA/distB)
       if b<self.y:
          angle = -angle
       return (math.cos(angle),math.sin(angle))



first_particle = Particle(100,100,10)


   
   
pygame.display.flip()
running = True

while running:
  pygame.display.flip()
  screen.fill(background_colour)
  first_particle.update()
  

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
