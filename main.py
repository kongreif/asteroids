import pygame
from pygame.locals import *

from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField

def main():
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    player_x = SCREEN_WIDTH / 2
    player_y = SCREEN_HEIGHT / 2

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    player = Player(player_x, player_y)

    Asteroid.containers = (asteroids, updateable, drawable)
    Shot.containers = (shots, updateable, drawable)

    AsteroidField.containers = (updateable)
    asteroid_field = AsteroidField()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        for item in updateable:
            item.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print('Game over!')
                exit()

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

        delta = clock.tick(60)
        dt = delta / 1000


if __name__ == "__main__":
    main()
