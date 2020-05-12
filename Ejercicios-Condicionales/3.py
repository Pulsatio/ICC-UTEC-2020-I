# Question 3
angulo_1 = int(input("angulo 1: "))
angulo_2 = int(input("angulo 2: "))
angulo_3 = int(input("angulo 3: "))
respuesta = " "
if angulo_1 == 90 and angulo_2 < 90 and angulo_3 < 90 and angulo_2+angulo_3 == 90:
    respuesta = "Si"
elif angulo_2 == 90 and angulo_1 < 90 and angulo_3 < 90 and angulo_1+angulo_3 == 90:
    respuesta = "Si"
elif angulo_3 == 90 and angulo_1 < 90 and angulo_2 < 90 and angulo_1+angulo_2 == 90:
    respuesta = "Si"
else:
    respuesta = "No"

print(respuesta, "es un triangulo rectangulo")