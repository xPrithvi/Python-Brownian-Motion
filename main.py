import pygame
import pymunk
import random

class Container():
    def __init__(self, point_1, point_2):
        self.body = pymunk.Body(body_type = pymunk.Body.STATIC)
        self.shape = pymunk.Segment(self.body, point_1, point_2, 5)
        self.shape.elasticity = 1
        space.add(self.shape)

class BulkParticle():
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.body = pymunk.Body()
        self.body.position = self.x_pos, self.y_pos
        self.body.velocity = random.uniform(-10, 10), random.uniform(-10, 10)
        self.shape = pymunk.Circle(self.body, 25)
        self.shape.density = 1
        self.shape.elasticity = 1
        space.add(self.body, self.shape)

    def draw(self):
        x_pos, y_pos = self.body.position
        pygame.draw.circle(GameDisplay, (255, 0, 0), (int(x_pos), int(y_pos)), 25)

class Particle():
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.body = pymunk.Body()
        self.body.position = self.x_pos, self.y_pos
        self.body.velocity = random.uniform(-100, 100), random.uniform(-100, 100)
        self.shape = pymunk.Circle(self.body, 5)
        self.shape.density = 1
        self.shape.elasticity = 1
        space.add(self.body, self.shape)

    def draw(self):
        x_pos, y_pos = self.body.position
        pygame.draw.circle(GameDisplay, (255, 255, 255), (int(x_pos), int(y_pos)), 5)

"""Pymunk Engine"""
space = pymunk.Space()

"""Pygame Simulation."""
pygame.init()

GameDisplay = pygame.display.set_mode((800,800))
pygame.display.set_caption("Brownian Motion")
clock = pygame.time.Clock()
FPS = 60
game_crashed = False

particles = [Particle(x_pos = random.randint(0, 800), y_pos = random.randint(0, 800)) for i in range(1000)]
bulk_particle = BulkParticle(x_pos = random.randint(0, 800), y_pos = random.randint(0, 800))
walls = [Container((0,0), (0,800)),
         Container((0,0), (800,0)),
         Container((0,800), (800,800)),
         Container((800,0), (800,800))]
while game_crashed == False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_crashed = True

    GameDisplay.fill((0, 0, 0))
    for particle in particles:
        particle.draw()
    bulk_particle.draw()

    pygame.display.update()
    clock.tick(FPS)
    space.step(1/FPS)

pygame.quit()
