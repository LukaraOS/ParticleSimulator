import pygame
import random 
import math 

background_colour = (255,255,255)
(width, height) = (1200, 800)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simulation')
screen.fill(background_colour)
black = (0,0,0)

box = pygame.Rect(400,200,400,400)
boxBorderLeft = 400
boxBorderTop = 200
boxBorderBot = 600
boxBorderRight = 800

class Particle:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.speed = 5
        self.angle = 0

        self.angle = math.pi / 11
        self.colour = (0, 0, 255)
        self.thickness = 1

    def display(self):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size, self.thickness)

    def move(self):
      self.x += math.sin(self.angle) * self.speed
      self.y -= math.cos(self.angle) * self.speed

    def bounce(self):
      """Checks for collision with box borders
      Calculates the new angle"""

      if self.x > boxBorderRight - self.size:
         self.x = 2 * (boxBorderRight - self.size) - self.x
         self.angle = - self.angle
      elif self.x < boxBorderLeft+self.size:
         self.x = 2 * (boxBorderLeft+self.size) - self.x
         self.angle = - self.angle
      if self.y > boxBorderBot - self.size:
         self.y = 2 * (boxBorderBot - self.size) - self.y
         self.angle = math.pi - self.angle
      elif self.y < boxBorderTop+self.size:
         self.y = 2 * (boxBorderTop + self.size) - self.y
         self.angle = math.pi - self.angle

    def moveTowardMouse(self,x,y):
       direction = self.findDir(x,y)
       self.x += direction[0]
       self.y += direction[1]
       
    def update(self):
       self.display()
       self.bounce()
       self.move()

    def findDir(self,x,y):
       delta_x = x - self.x
       delta_y = y - self.y

       return (1/50 * delta_x, 1/50 * delta_y)
       
def refresh_screen(particle):
   pygame.display.flip()
   
   screen.fill(background_colour)
   pygame.draw.rect(screen,black,box,1)
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

