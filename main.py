import pygame
import sys
from asteroidfield import AsteroidField
from asteroid import Asteroid
import circleshape
from constants import SCREEN_WIDTH,SCREEN_HEIGHT
from logger import log_state,log_event
from player import Player
from circleshape import CircleShape
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids,updatable,drawable)
    Player.containers = (updatable,drawable)
    Shot.containers = (shots,drawable,updatable)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen) 
        pygame.display.flip()
        updatable.update(dt)
        for obj in asteroids:
            if player.collides_with(obj):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        dt = clock.tick(60)/1000
if __name__ == "__main__":
    main()
