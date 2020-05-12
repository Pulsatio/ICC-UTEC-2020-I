while 1:
	lado = int(input("Ingrese el lado del cuadrado: "))
	if 5<=lado and lado<=10:
		break
for i in range(lado):
	for j in range(lado):
		if i==0 or j==0 or i==lado-1 or j==lado-1 or i==j or i+j==lado-1:
			print("*",end="")
		else:
			print(" ",end="")
	print()