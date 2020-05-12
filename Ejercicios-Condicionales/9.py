# Question 9
mes = int(input("Mes: "))
dia = int(input("Dia: "))
respuesta = " "
if (mes == 12 and dia >= 21) or (mes >= 1 and mes < 3) or (mes == 3 and dia <= 20):
    respuesta = "Verano"
elif (mes == 3 and dia >= 21) or (mes > 3 and mes < 6) or (mes == 6 and dia <= 21):
    respuesta = "Otoño"
elif (mes == 6 and dia >= 22) or (mes > 6 and mes < 9) or (mes == 9 and dia <= 22):
    respuesta = "Invierno"
elif (mes == 9 and dia >= 23) or (mes > 9 and mes < 12) or (mes == 12 and dia <= 20):
    respuesta = "Primavera"

print("Estacion: ", respuesta)