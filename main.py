import pygame
from asteroidfield import AsteroidField
from asteroid import Asteroid
from constants import SCREEN_WIDTH,SCREEN_HEIGHT
from logger import log_state
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids,updatable,drawable)
    Player.containers = (updatable,drawable)
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
       
        #print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
        #print(f"Screen width: {SCREEN_WIDTH}")
        #print(f"Screen height: {SCREEN_HEIGHT}")
        updatable.update(dt)
        dt = clock.tick(60)/1000
        print(dt)
if __name__ == "__main__":
    main()
