size = int(input("Ingrese un numero: "))

for i in range(1, size+1):
	
	print(i, end=" " )
	
	for j in range(1, i+1):
		
		if not((j+i) % 2):
			print("*", end="")
		else:
			print(" ", end="")
	print()
