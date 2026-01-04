import pygame

from random import uniform

from logger import log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            degrees = uniform(20, 50)
            asteroid1_vel = pygame.math.Vector2.rotate(self.velocity, degrees)
            asteroid2_vel = pygame.math.Vector2.rotate(self.velocity, -degrees)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(
                self.position.x,
                self.position.y,
                new_radius,
            )
            asteroid2 = Asteroid(
                self.position.x,
                self.position.y,
                new_radius,
            )
            asteroid1.velocity = asteroid1_vel * 1.2
            asteroid2.velocity = asteroid2_vel * 1.2
