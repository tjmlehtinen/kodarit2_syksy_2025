import pygame
import sys

pygame.init()

NAYTTO = pygame.display.set_mode((600, 400))

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    NAYTTO.fill((123,163,233))
    (x, y) = pygame.mouse.get_pos()
    pygame.draw.rect(NAYTTO, (255, 0, 0), (x, y, 10, 200))
    pygame.display.update()

pygame.quit()