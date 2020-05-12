# Question 2

respuesta = " "
numero = int(input("Ingrese un número: "))
if numero > 0:
    respuesta = "Es positivo."
elif numero < 0:
    respuesta = "Es negativo."
else:
    respuesta = "Es cero."

print(respuesta)