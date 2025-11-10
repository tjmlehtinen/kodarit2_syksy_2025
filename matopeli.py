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
suunta = ALAS

# madon liikuttaminen
def liikuta_matoa():
    # otetaan madon pään koordinaatit talteen
    paa_x, paa_y = mato[-1]
    # lasketaan uusi pää
    if suunta == ALAS:
        uusi_paa = (paa_x, paa_y + 1)
    elif suunta == OIKEA:
        uusi_paa = (paa_x + 1, paa_y)
    elif suunta == VASEN:
        uusi_paa = (paa_x - 1, paa_y)
    elif suunta == YLOS:
        uusi_paa = (paa_x, paa_y - 1)
    # lisätään uusi pää matoon
    mato.append(uusi_paa)
    # poistetaan madon viimeinen pala
    mato.pop(0)

# meneekö mato yli reunan
def mato_yli_reunan():
    paa_x, paa_y = mato[-1]
    if paa_x < 0:
        return True
    return False

# kello
kello = pygame.time.Clock()

# peliluuppi
while True:
    # nopeus eli kertoja sekunnissa
    kello.tick(3)
    # tapahtumat
    for tapahtuma in pygame.event.get():
        # onko lopetus
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # onko tapahtuma näppäimen painallus
        if tapahtuma.type == pygame.KEYDOWN:
            # onko näppäin nuoli oikealle
            if tapahtuma.key == pygame.K_RIGHT:
                suunta = OIKEA
            # nuoli vasemmalle
            elif tapahtuma.key == pygame.K_LEFT:
                suunta = VASEN
            # nuoli alas
            elif tapahtuma.key == pygame.K_DOWN:
                suunta = ALAS
            # nuoli ylös
            elif tapahtuma.key == pygame.K_UP:
                suunta = YLOS
    piirra_tausta()
    piirra_mato()
    pygame.display.update()
    liikuta_matoa()
    if mato_yli_reunan():
        break

pygame.quit()