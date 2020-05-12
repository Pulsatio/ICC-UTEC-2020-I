# Question 1

numero_1 = int(input("Ingrese un número 1: "))
numero_2 = int(input("Ingrese un número 2: "))
numero_3 = int(input("Ingrese un número 3: "))
numero_4 = int(input("Ingrese un número 4: "))

pares = 0
if numero_1 % 2 == 0:
    pares += 1
if numero_2 % 2 == 0:
    pares += 1
if numero_3 % 2 == 0:
    pares += 1
if numero_4 % 2 == 0:
    pares += 1

respuesta = " "
if pares == 0:
    respuesta = "Cero pares"
elif pares == 1:
    respuesta = "Un par"
elif pares == 2:
    respuesta = "Dos pares"
elif pares == 3:
    respuesta = "Tres pares"
else:
    respuesta = "Cuatro pares"

print("Respuesta: ", respuesta)

