import pygame
import sys

pygame.init()

# pelin koko
RUUTU = 20
LEVEYS = 20
KORKEUS = 15

# näyttö
NAYTON_KOKO = (LEVEYS * RUUTU, KORKEUS * RUUTU)
NAYTTO = pygame.display.set_mode(NAYTON_KOKO)
pygame.display.set_caption("MATOPELI")

# värit
taustavari = pygame.Color(0, 0, 130)

# ruudun piirtäminen
def piirra_ruutu(x, y, vari):
    ylakulma = (x * RUUTU + 1, y * RUUTU + 1)
    koko = (RUUTU - 2, RUUTU - 2)
    pygame.draw.rect(NAYTTO, vari, )

# peliluuppi
while True:
    # tapahtumat
    for tapahtuma in pygame.event.get():
        # onko lopetus
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    NAYTTO.fill(taustavari)
    pygame.display.update()

pygame.quit()