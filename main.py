import pygame
import fly
from sys import exit


pygame.init()
screen = pygame.display.set_mode((1280, 720))
screen.fill('black')
pygame.mouse.set_visible(False)
pygame.mouse.set_pos((640,360))
clock = pygame.time.Clock()

border = pygame.Rect(300, 300, 1110, 550)
border.center = (640, 360)


fly_group = pygame.sprite.GroupSingle()
fly_group.add(fly.Fly())



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill('black')
    print(pygame.mouse.get_rel())
    pygame.draw.rect(screen, 'red', border, width=3, border_radius=4)
    fly_group.draw(screen)
    fly_group.update()
    pygame.display.update()
    clock.tick(60)