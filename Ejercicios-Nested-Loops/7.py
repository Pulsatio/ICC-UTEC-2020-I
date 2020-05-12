lado = 0
while lado<5 or lado>10 :
	lado = int(input("Ingrese el lado de un cuadrado:"))

for y in range(lado):
	for x in range(lado):
		if y==0 or y==lado-1 or x==0 or \
		x==lado-1 or x==y or x==(lado-(y+1)) :
			print("*", end= "")
		else:
			print(" ", end= "")
	print()