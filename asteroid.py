from circleshape import CircleShape
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
from logger import log_event
import random
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        new_vector_a = self.velocity.rotate(angle)
        new_vector_b = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        splitted_asteroid_a = Asteroid(self.position[0], self.position[1], new_radius)
        splitted_asteroid_b = Asteroid(self.position[0], self.position[1], new_radius)
        splitted_asteroid_a.velocity = new_vector_a * 1.2
        splitted_asteroid_b.velocity = new_vector_b * 1.2
