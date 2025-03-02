import pygame
import random 
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

class Particle:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.speed = 1
        self.angle = 0

        self.angle = -math.pi/2 
        self.colour = (0, 0, 255)
        self.thickness = 1

    def display(self):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size, self.thickness)

    def move(self):
      """Increments x and y position coordinates"""

      self.x += math.cos(self.angle) * self.speed
      self.y += math.sin(self.angle) * self.speed


    def bounce(self):
      """Checks for collision with box borders
      Calculates the new angle"""

      if self.x > boxBorderRight - self.size:
         self.x = 2 * (boxBorderRight - self.size) - self.x
         self.angle = math.pi - self.angle

      elif self.x < boxBorderLeft+self.size:
         self.x = 2 * (boxBorderLeft+self.size) - self.x
         self.angle = math.pi - self.angle

      if self.y > boxBorderBot - self.size:
         self.y = 2 * (boxBorderBot - self.size) - self.y
         self.angle = -self.angle

      elif self.y < boxBorderTop+self.size:
         self.y = 2 * (boxBorderTop + self.size) - self.y
         self.angle = -self.angle

    def moveTowardMouse(self):
       """Main movement method
       Checks for mouse presence in box
       Calls movement based on mouse position"""
       position = pygame.mouse.get_pos()
       
       if position[0]<boxBorderLeft or position[0]>boxBorderRight or position[1]>boxBorderBot or position[1]<boxBorderTop:         
          self.move()

       else:
         if position[1] >= self.y:
            self.angle = self.findAngle(position[0],position[1])
         else:
            self.angle = self.findAngle(position[0],position[1])*-1
         self.move()

       
    def update(self):
       self.display()
       self.bounce()
       self.moveTowardMouse()

    def findAngle(self,x,y):
      """Finds angle between particle center
      and a point (x,y)
      Returns an angle between 0 and Pi"""

      direct = (x-self.x,math.sqrt((y-self.y)**2+(x-self.x)**2)) 
      angle = math.acos(direct[0]/direct[1])
      return angle
      

    def findDir(self,x,y):
       """Finds vector toward point x,y"""
       delta_x = x - self.x
       delta_y = y - self.y

       return (1/50 * delta_x, 1/50 * delta_y)
   
first_particle = Particle(100,100,20)
second_particle = Particle(200,150,12)

Particle_List = []
Particle_List.append(first_particle)
Particle_List.append(second_particle)
running = True

while running:
  for particle in Particle_List:
     particle.update() 
  pygame.display.flip()
  screen.fill(background_colour)
  pygame.draw.rect(screen,black,box,1)
  position = pygame.mouse.get_pos()
  print(f"The position of the mouse is -> {position}")

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

