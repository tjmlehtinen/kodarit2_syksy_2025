print("Lisäillään listalle asioita!")
asiat = []
while True:
    asia = input("Anna listalle lisättävä asia, tyhjä lisäys lopettaa\n")
    if asia == "":
        break
    else:
        asiat.append(asia)
print("Lisäsit listalle " + str(len(asiat)) + " asiaa")
print("Lisäsit seuraavat asiat:")
for asia in asiat:
    print(asia)