# Question 8
num_1 = int(input("Ingrese el primer numero: "))
num_2 = int(input("Ingrese el segundo numero: "))

opcion = input("Ingrese la opción: ")
if opcion == 'a':
    print("El area del triangulo es: ", num_1 * num_2 / 2)
elif opcion == 'b':
    print("El promedio de ", num_1, "y ", num_2, " es: ", (num_1+num_2)/2)
elif opcion == 'c':
    if num_2 == 0:
        print("B no puede ser 0")
    else:
        print("La division de ", num_1, " entre",
              num_2, " es: ", num_1 / num_2)
elif opcion == 'd':
    if num_1 > num_2:
        print("El mayor numero es: ", num_1)
    else:
        print("El mayor numero es: ", num_2)