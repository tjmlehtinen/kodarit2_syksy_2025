# ladataan tarvittavat kirjastot
import pygame
import sys

# alustetaan pygame
pygame.init()

# määritellään näyttö
LEVEYS = 600
KORKEUS = 400
NAYTTO = pygame.display.set_mode((LEVEYS, KORKEUS))
pygame.display.set_caption("KOITA SELVITÄ!")

# taustan piirtäminen
def piirra_tausta():
    NAYTTO.fill((0, 133, 90))
    pygame.draw.circle(NAYTTO, (233, 233, 133), (100, 100), 30)
    pygame.draw.circle(NAYTTO, (233, 233, 133), (500, 150), 40)
    pygame.draw.circle(NAYTTO, (233, 233, 133), (400, 200), 20)
    pygame.draw.circle(NAYTTO, (233, 233, 133), (200, 300), 50)

# pelaajan määrittely
pelaaja = pygame.Rect((0, 0), (50, 50))
pelaajan_vari = pygame.Color(255, 0, 255)

# kimpoilijan määrittely
kimpoilija = pygame.Rect((300, 300), (50, 50))
kimpoilijan_vari = pygame.Color(0, 255, 255)
kimpoilijan_muutos_x = 2
kimpoilijan_muutos_y = 3

def paivita_kimpoilija():
    global kimpoilijan_muutos_x
    global kimpoilijan_muutos_y
    # liikutetaan kimpoilijaa
    kimpoilija.move_ip(kimpoilijan_muutos_x, kimpoilijan_muutos_y)
    # osuuko vasempaan tai oikeaan laitaan
    if kimpoilija.left < 0 or kimpoilija.right > LEVEYS:
        kimpoilijan_muutos_x *= -1
    # osuuko ylös tai alas
    if kimpoilija.top < 0 or kimpoilija.bottom > KORKEUS:
        kimpoilijan_muutos_y *= -1

# kello pelin nopeutta säätämään
kello = pygame.time.Clock()

# peliluuppi
while True:
    # asetetaan fps eli kuinka monta kertaa sekunnissa päivitetään
    kello.tick(40)
    # käydään läpi tapahtumat
    for tapahtuma in pygame.event.get():
        # tarkistetaan onko tapahtuma ikkunan sulkeminen
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    piirra_tausta()
    # pelaajan sijainti hiiren kohdalle
    pelaaja.center = pygame.mouse.get_pos()
    # pelaajan piirtäminen
    pygame.draw.rect(NAYTTO, pelaajan_vari, pelaaja)
    # kimpoilijan liikuttaminen ja piirtäminen
    paivita_kimpoilija()
    pygame.draw.rect(NAYTTO, kimpoilijan_vari, kimpoilija)
    # päivitetään näyttö
    pygame.display.update()
    if pelaaja.colliderect(kimpoilija):
        break

# sulkee pygamen
pygame.quit()