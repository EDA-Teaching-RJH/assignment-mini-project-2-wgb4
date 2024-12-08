import math
import pygame

# A generic 'Particle' type, which will be used as a template for more specific material types

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, "red", (int(self.x), int(self.y)), 1)
        