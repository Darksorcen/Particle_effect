import pygame
import random 
import math

from particles import Particle

pygame.init()

screen = pygame.display.set_mode((360, 360), pygame.RESIZABLE, 32)
clock = pygame.time.Clock()

# [loc, velocity, timer, color]
particles = []
i = 0

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pos = pygame.mouse.get_pos()
    i += 0.005
    if i == 361:
        i = 0

    screen.fill((0, 0 ,0))
    random_color = [0, 0, random.randint(0, 255)]

    particles.append(Particle(list(pos), [random.randint(0, 20) / 10 - 1, random.randint(0, 10) / 5 - 1], 
                                          random.randint(6, 8), random_color, [False, True, False, False]))

    for particle in particles:
        particle.update(special_movement=[math.cos(i), math.sin(-i)])
        if particle.timer == 0 or particle.check_particle_on_screen(screen):
            particles.remove(particle)
        else:
            particle.display(screen)
    pygame.display.update(screen.get_rect())
    clock.tick(60)
    #print(clock.get_fps())