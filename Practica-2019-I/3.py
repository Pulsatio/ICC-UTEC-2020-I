lista = []
while 1:
	numero = int(input())
	if numero==0:
		break
	if numero%2==0:
		lista.append(numero)
print(lista)