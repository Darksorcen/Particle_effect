import pygame, random, math

pygame.init()

screen = pygame.display.set_mode((360, 360), pygame.RESIZABLE, 32)
clock = pygame.time.Clock()

# [loc, velocity, timer, color]
particles = []
i = 0

def check_particle_on_screen(particle):
    return (particle[0][0] > screen.get_width() or particle[0][1] > screen.get_height() or particle[0][0] < 0 or particle[0][1] < 0)

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

    particles.append([list(pos), [random.randint(0, 20) / 10 - 1, -2], random.randint(6, 8), random_color])

    for particle in particles:
        particle[0][0] += math.cos(i)*particle[1][0]
        particle[0][1] += math.sin(-i)*particle[1][1]
        particle[2] -= 0.01
        #particle[1][1] += 0.1
        pygame.draw.rect(screen, particle[3], pygame.Rect(particle[0][0], particle[0][1], particle[2], particle[2]))
        if particle[2] <= 0 or check_particle_on_screen(particle):
            particles.remove(particle)
    pygame.display.update(screen.get_rect())
    clock.tick(60)
    print(clock.get_fps())