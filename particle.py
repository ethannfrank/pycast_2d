import math

import pygame.math

from settings import *
from ray import Ray


class Particle:

    def __init__(self):
        self.pos = pygame.math.Vector2(100, 100)
        self.rays = []
        for a in range(0, 360, 1):
            self.rays.append(Ray(self.pos, math.radians(a)))

    def update(self, x, y):
        self.pos.x = x
        self.pos.y = y

    def look(self, window, walls):
        for ray in self.rays:
            closest = None
            record = math.inf
            for wall in walls:
                pt = ray.cast(wall)
                if pt:
                    d = pygame.Vector2.distance_to(self.pos, pt)
                    if d < record:
                        record = d
                        closest = pt
            if closest:
                # c = math.hypot(closest.x, closest.y)
                # percent = c / 1468.6
                # alpha = round(percent * 255)
                pygame.draw.line(window, WHITE, self.pos, closest)

    def show(self, window):
        for ray in self.rays:
            ray.show(window)
        pygame.draw.circle(window, WHITE, (self.pos.x, self.pos.y), 4)