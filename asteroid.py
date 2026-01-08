from random import Random, random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)
        
    def update(self, dt):
        self.position += self.velocity * dt  

    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        new_angel = random.uniform(20,50)
        print(f"new_angel:",new_angel)
        first_ast_rot = pygame.math.Vector2.rotate(self.velocity,new_angel)
        print("first_ast_rot",first_ast_rot)
        sec_ast_rot =  pygame.math.Vector2.rotate(-self.velocity,-new_angel) 
        print("sec_ast_rot :",sec_ast_rot)
        self.radius = self.radius - ASTEROID_MIN_RADIUS
        print(self.radius)
        Asteroid(self.position,new_angel,new_angel)        



