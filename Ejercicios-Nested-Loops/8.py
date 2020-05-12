N = int(input("Ingrese un número: "))

for j in range(N):
	for i in range(N):
		if i==0 or j==N-1 or i==j:
			print("*", end="")
		else:
			print(" ", end="")
	print()