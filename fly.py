import pygame.sprite


class Fly(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Sprites/1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()/5, self.image.get_height()/5))
        self.rect = self.image.get_rect(center = (670, 360))
        self.move = True


    def movement(self):
        mouse_pos = pygame.mouse.get_pos()
        if not (mouse_pos[0] > 1150 or mouse_pos[0] < 100 or mouse_pos[1] > 600 or mouse_pos[1] < 100):
            self.rect.center = mouse_pos

    def flip_char(self):
        relative_mov = pygame.mouse.get_rel()
        if relative_mov[0] > 0 and self.move:
            self.image = pygame.transform.flip(self.image, True, True)
            self.move = False

    def update(self):
        self.movement()
        self.flip_char()