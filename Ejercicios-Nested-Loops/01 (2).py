size = int(input("Ingrese el valor de N: "))

for i in range(1, size+1):
	for j in range(1, i+1):
		print("*", end="")
	print()
