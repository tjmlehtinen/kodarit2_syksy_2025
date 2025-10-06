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
    NAYTTO.fill((0, 133, 0))
    pygame.draw.circle(NAYTTO, (233, 233, 133), (100, 100), 30)
    pygame.draw.circle(NAYTTO, (233, 233, 133), (500, 150), 40)
    pygame.draw.circle(NAYTTO, (233, 233, 133), (400, 200), 20)
    pygame.draw.circle(NAYTTO, (233, 233, 133), (200, 300), 50)

# peliluuppi
while True:
    # käydään läpi tapahtumat
    for tapahtuma in pygame.event.get():
        # tarkistetaan onko tapahtuma ikkunan sulkeminen
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    piirra_tausta()
    # päivitetään näyttö
    pygame.display.update()

# sulkee pygamen
pygame.quit()