tamano = 4
while(tamano < 5 or tamano > 10):
    tamano = int(input("Ingrese el lado de un cuadrado: "))

print("* " * tamano)
x = tamano-2
for i in range(x):

    print("*", end=' ')
    for j in range(x):
        if not(i-j) or not(i+j-tamano + 3):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("*")

print("* " * tamano)
