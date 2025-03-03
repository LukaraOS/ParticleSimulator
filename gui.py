import pygame
import math


class Screen:
  def __init__(self,width,height,boxSize):
    self.width = width
    self.height = height

    #MAIN BOX DEFINITION
    self.boxSize = boxSize
    self.box = pygame.Rect((self.width-self.boxSize)/2,(self.height-self.boxSize)/2,self.boxSize,self.boxSize)
    self.background_colour = (255,255,255)
    
    self.boxBorderLeft = self.box.left
    self.boxBorderTop = self.box.top
    self.boxBorderBot = self.box.bottom
    self.boxBorderRight = self.box.right

  def drawBox(self): #Draw our box 
    pygame.draw.rect(self.screen,(0,0,0),self.box,1)

  def show(self): #Call this first to init the screen 
    self.screen = pygame.display.set_mode((self.width,self.height))
    self.update()

  def update(self):
    pygame.display.flip()
    self.screen.fill(self.background_colour)
    self.drawBox()


screen = Screen(1200,800,400)
screen.show()
running = True
while running:
  screen.update()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

