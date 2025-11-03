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
taustavari = pygame.Color(205, 133, 63)
taustaruutuvari = pygame.Color(244, 164, 96)
matovari = pygame.Color(0, 130, 0)

# ruudun piirtäminen
def piirra_ruutu(x, y, vari):
    ylakulma = (x * RUUTU + 1, y * RUUTU + 1)
    koko = (RUUTU - 2, RUUTU - 2)
    pygame.draw.rect(NAYTTO, vari, (ylakulma, koko))

# taustan piirtäminen
def piirra_tausta():
    NAYTTO.fill(taustavari)
    for x in range(LEVEYS):
        for y in range(KORKEUS):
            piirra_ruutu(x, y, taustaruutuvari)

# mato
mato = [(0,0), (0,1), (0,2), (0,3)]

# madon piirtäminen
def piirra_mato():
    for madon_osa in mato:
        x, y = madon_osa
        piirra_ruutu(x, y, matovari)

# suunnat
ALAS = 0
VASEN = 1
YLOS = 2
OIKEA = 3

# peliluuppi
while True:
    # tapahtumat
    for tapahtuma in pygame.event.get():
        # onko lopetus
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    piirra_tausta()
    piirra_mato()
    pygame.display.update()

pygame.quit()