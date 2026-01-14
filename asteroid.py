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
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        new_angle = random.uniform(20,50)
        print(f"new_angle:",new_angle)
        first_ast_rot = self.velocity.rotate(new_angle)
        print("first_ast_rot",first_ast_rot)
        sec_ast_rot =  self.velocity.rotate(-new_angle)
        print("sec_ast_rot :",sec_ast_rot)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        print(new_radius)
        asteroid = Asteroid(self.position.x,self.position.y,new_radius)
        asteroid.velocity= first_ast_rot*1.2
        #Asteroid(self.position,sec_ast_rot,new_radius).velocity.update(sec_ast_rot*1.2) 
        asteroid = Asteroid(self.position.x,self.position.y,new_radius)
        asteroid.velocity= sec_ast_rot*1.2


