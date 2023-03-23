import pygame.sprite


class border(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.border = pygame.Rect(300, 300, 1110, 550)
        self.border.center = (640, 360)
