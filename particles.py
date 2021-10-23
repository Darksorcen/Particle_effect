import pygame

class Particle:

    def __init__(self, pos, velocity, timer, color, shape_bool):
        self.pos = pos
        self.velocity = velocity
        self.timer = timer
        self.color = color
        self.gravity = 0
        self.shape_bool = shape_bool 
        self.shape = {"circle":[shape_bool[0]], 
                      "rect":[shape_bool[1], pygame.Rect(self.pos[0], self.pos[1], self.timer, self.timer)],
                      "triangle":[shape_bool[2], [[self.pos[0], self.pos[1]], [self.pos[0]+5, self.pos[1]-5], [self.pos[0]+10, self.pos[1]]]],
                      "polygon":[shape_bool[3], [[self.pos[0], self.pos[1]], [self.pos[0]+4, self.pos[1]+4], 
                                                [self.pos[1]+4, self.pos[0]+4], [self.pos[0]-4, self.pos[1]-4]]]}
        self.original_shape = self.shape

    def set_shape(self, name, shape):
        self.shape[name] = shape

    def update(self, gravity_force=0, special_movement=[1, 1]):
        self.pos[0] += self.velocity[0]*special_movement[0]
        self.pos[1] += self.velocity[1]*special_movement[1]
        self.timer -= 0.01
        self.velocity[1] += self.gravity+gravity_force
        self.gravity += gravity_force/10
        self.shape = {"circle":[self.shape_bool[0]], 
                      "rect":[self.shape_bool[1], pygame.Rect(self.pos[0], self.pos[1], self.timer, self.timer)],
                      "triangle":[self.shape_bool[2], [[self.pos[0], self.pos[1]], [self.pos[0]+5, self.pos[1]-5], [self.pos[0]+10, self.pos[1]]]],
                      "polygon":[self.shape_bool[3], [[self.pos[0], self.pos[1]], [self.pos[0]+4, self.pos[1]+4], 
                                                      [self.pos[1]+4, self.pos[0]+4], [self.pos[0]-4, self.pos[1]-4]]]}

    def display(self, screen):
        for key, value in self.shape.items():
            if value[0]:
                if key == "circle":
                    pygame.draw.circle(screen, self.color, self.pos, self.timer)
                if key == "rect":
                    pygame.draw.rect(screen, self.color, self.shape[key][1])
                if key == "triangle":
                    pygame.draw.polygon(screen, self.color, self.shape[key][1])
                if key == "polygon":
                    pygame.draw.polygon(screen, self.color, self.shape[key][1])

    def check_particle_on_screen(self, screen):
        return (self.pos[0] > screen.get_width() or self.pos[0] < 0 or self.pos[1] > screen.get_height() or self.pos[1] < 0)