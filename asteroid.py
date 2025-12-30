import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen,pygame.color,pos,radius,LINE_WIDTH)
        
    def update(self, dt):
        self.move(dt)
        pos =self.velocity + self.velocity * dt  


