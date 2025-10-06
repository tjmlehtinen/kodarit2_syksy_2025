import random

print("Tämä on numeron arvaamis peli")
arvattava_luku = random.randint(1, 100)
print(arvattava_luku)
on_arvattu = False
while not on_arvattu:
    pelaajan_arvaus = int(input("Arvaa luku 1-100:\n"))
    if pelaajan_arvaus == arvattava_luku:
        print("Oikein!")
        on_arvattu = True
    elif pelaajan_arvaus < arvattava_luku:
        print("Luku on liian pieni")
    else:
        print("Luku on liian suuri")
