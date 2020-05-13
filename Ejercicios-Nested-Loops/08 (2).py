
size = int(input("Ingrese un numero: "))

for i in range(1, size):
	
	print(i, end=" " )
	
	print("*", end="")
	for j in range(1, i-1):
		print(" ", end="")
		
	if i != 1:
		print("*", end="")
	print()
print(str(size), "*"* size)

