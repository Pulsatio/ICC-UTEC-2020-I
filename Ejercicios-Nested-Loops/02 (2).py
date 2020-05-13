limit = int(input("Ingrese el numero: "))

for i in range(1, limit+1):
	for j in range(1, 10):
		print(str(i) + "*" + str(j) + " = " + str(i*j))	
