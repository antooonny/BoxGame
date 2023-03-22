import pygame.sprite


class Fly(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Sprites/1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()/5, self.image.get_height()/5))
        self.rect = self.image.get_rect(center = (670, 360))

    def movement(self):
        mouse_pos = pygame.mouse.get_pos()
        self.rect.center = mouse_pos
    def update(self):
        self.movement()