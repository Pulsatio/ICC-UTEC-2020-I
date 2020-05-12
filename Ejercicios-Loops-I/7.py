suma=0
while 1:
	numero = int(input("Ingrese un numero: "))
	if numero<0: 
		break 
	if numero%3==0 or numero%4==0:
		suma+=numero
print(suma)