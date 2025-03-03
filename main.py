import pygame as pygame 

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, vec1):
        vec2 = Vector2(self.x + vec1.x, self.y + vec1.y)
        return vec2
    
    def __neg__(self): 
        vec1 = Vector2(-self.x,-self.y)
        return vec1
    
    def __str__(self): #Defines the output upon calling str method on a Vector2 object i.e : print( Vector2 object ) --> (x,y)
        coordinates = f"({self.x},{self.y})"
        return coordinates
    
    def __mul__(self, vec1): # /!\ Dot Product not Vectorial Product /!\
        dotProduct = self.x * vec1.x + self.y * vec1.y     
        return dotProduct
    
    def __sub__(self, vec1):
        vec2 = Vector2(self.x - vec1.x, self.y - vec1.y)
        return vec2

class Particle:
    def __init__(self, x, y):
        self.position = Vector2(x,y)
        self.acceleration = Vector2(-1,-1)
        self.velocity = Vector2(1,1)
        self.gravity = Vector2(0,-9.81)
    
    def movement(self):
        self.velocity = self.velocity + self.acceleration
        self.position = self.position + self.velocity + self.gravity
        


particle = Particle(0,0)


for i in range(100):
    particle.movement()

    print(particle.position)

