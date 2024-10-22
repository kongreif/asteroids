import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.velocity = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius < ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)
        velocity_split_1 = self.velocity.rotate(angle) * 1.2
        velocity_split_2 = self.velocity.rotate(-angle) * 1.2

        split_radius = self.radius - ASTEROID_MIN_RADIUS

        split_1 = Asteroid(self.position.x, self.position.y, split_radius)
        split_2 = Asteroid(self.position.x, self.position.y, split_radius)

        split_1.velocity = velocity_split_1
        split_2.velocity = velocity_split_2
