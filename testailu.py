for i in range(5):
    print(i)
    if i < 2:
        print("hei")
    else:
        print("moi")

nimi = input("Mikä on nimesi?\n")
montako = int(input("Montako moita?\n"))
for i in range(montako):
    print("Moi " + nimi + "!")