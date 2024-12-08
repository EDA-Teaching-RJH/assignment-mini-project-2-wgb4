# A sand pit creator on pygame

import pygame
import particles

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
dt = 0

particles = [particles.Particle(300, 300)]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for particle in particles:
        particle.draw(screen)

    pygame.display.flip()

    dt = clock.tick(60) / 1000


pygame.quit()