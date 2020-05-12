# Question 5
respuesta = " "
trump_number = int(input("Ingrese un numero: "))
if trump_number < 0:
    respuesta = "Es"
elif trump_number > 0:
    if trump_number % 3 == 0 and trump_number % 6 != 0:
        respuesta = "Es"
    elif trump_number >= 100 and trump_number - ((trump_number // 10) * 10) == 1:
        respuesta = "Es"
    else:
        respuesta = "No es"

print(respuesta+" tramposo")