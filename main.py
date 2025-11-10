import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from logger import log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
pygame.init()


def main():

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    dt = 0
    clock = pygame.time.Clock()


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroidfield = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()
    new_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    pygame.sprite.Sprite.kill(shot)
                    asteroid.split()
            if asteroid.collides_with(new_player):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()

        for icon in drawable:
            icon.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60) / 200




#with pygame version: (%s) ' %  pygame.version.ver
if __name__ == "__main__":
    main()
