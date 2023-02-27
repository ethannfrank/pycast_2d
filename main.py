import random
import sys
import pygame

from boundary import Boundary
from particle import Particle
from settings import *

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PyCast")

walls = []
particle = Particle()
for i in range(0, NUM_WALLS):
    x1 = random.randint(0, WIDTH)
    y1 = random.randint(0, HEIGHT)
    x2 = random.randint(0, WIDTH)
    y2 = random.randint(0, HEIGHT)
    walls.append(Boundary(x1, y1, x2, y2))
walls.append(Boundary(1, 1, WIDTH-1, 1))
walls.append(Boundary(WIDTH-1, 1, WIDTH-1, HEIGHT-1))
walls.append(Boundary(WIDTH-1, HEIGHT-1, 1, HEIGHT-1))
walls.append(Boundary(1, HEIGHT, 1, 1))


def draw():
    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]
    window.fill(BLACK)

    for wall in walls:
        wall.show(window)
    particle.update(mouseX, mouseY)
    particle.look(window, walls)
    particle.show(window)

    # ray.show(window)
    # ray.lookAt(mouseX, mouseY)

    # pt = ray.cast(wall)
    # if pt:
    #     pygame.draw.circle(window, WHITE, (pt.x, pt.y), 8)
    pygame.display.update()


def setup():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        draw()


if __name__ == "__main__":
    setup()