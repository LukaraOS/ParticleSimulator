import pygame
import random 

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

particles_list = []
particles_number = 10
for i in range(particles_number):
    size = random.randint(10,20)
    new_particle = Particle(random.randint(size,width-size),random.randint(size,height-size),size)
    particles_list.append(new_particle)

for particle in particles_list:
    particle.display()

pygame.display.flip()
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

