# Question 7

edad = int(input("Ingresa tu edad: "))
clan = input("Ingresa tu clan: ")

if edad >= 15:
    if clan == "pretino":
        bono = 500
        print("Te corresponde un bono de", bono, "estufares")
    elif clan == "toriente":
        bono = 600
        print("Te corresponde un bono de", bono, "estufares")
    elif clan == "folunta":
        bono = 700
        print("Te corresponde un bono de", bono, "estufares")
else:
    print("No te corresponde bono")