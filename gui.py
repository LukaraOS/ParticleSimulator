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
        self.speed = 1
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

    def moveTowardMouse(self):
       position = pygame.mouse.get_pos()
       if position[0]<boxBorderLeft or position[0]>boxBorderRight or position[1]>boxBorderBot or position[1]<boxBorderTop:
          self.move()
       else:
         self.bounce()
         self.angle = self.findAngle(position[0],position[1])
         self.move()
         #self.x += math.sin(self.angle) * self.speed
         #self.y -= math.cos(self.angle) * self.speed
       
    def update(self):
       self.display()
       self.bounce()
       self.moveTowardMouse()

    def findAngle(self,x,y):
      """director_Vector = (1,0)
      dotProduct = x
      dist = math.sqrt((self.x+x)**2+(self.y+y)**2)
      angle = math.acos(dotProduct/dist)"""

      direct = (x-self.x,y-self.y) 
      angle = math.atan2(direct[1],direct[0])
      return angle
      

    def findDir(self,x,y):
       """Finds vector toward point x,y"""
       delta_x = x - self.x
       delta_y = y - self.y

       return (1/50 * delta_x, 1/50 * delta_y)
       
def refresh_screen(particle):
  
   particle.update()

first_particle = Particle(100,100,10)
second_particle = Particle(200,150,12)

running = True

while running:
  refresh_screen(first_particle)
  refresh_screen(second_particle)
  pygame.display.flip()
  screen.fill(background_colour)
  pygame.draw.rect(screen,black,box,1)
  position = pygame.mouse.get_pos()
  print(f"The position of the mouse is -> {position}")

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

