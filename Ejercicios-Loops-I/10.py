N = int(input("ingrese el numero de votantes: "))

votos_A = 0
votos_B = 0
votos_C = 0


for i in range(N):
	voto = input("Por quien vota?: ")
	clan = input("Clan?: ")
	if clan == 'toriente':
		sumar = 2	
	elif clan == 'folunta':
		sumar = 3
	else: 
		sumar = 1
	if voto == 'A':
		votos_A += sumar
	elif voto == 'B':
		votos_B += sumar
	else:
		votos_C += sumar
	if votos_A > votos_B and votos_A > votos_C:
		mayor = 'A'
	elif votos_C > votos_A and votos_C > votos_B:
		mayor = 'C'
	else:
		mayor = 'B'
print("Ganador:", mayor)
	

		
	
