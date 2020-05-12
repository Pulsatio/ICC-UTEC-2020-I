N = int(input("ingrese un número: "))

for j in range(N):
	for i in range(N):
		if i<=j:
			if (i+j+1)%2:
				print("*", end="")
			else:
				print(" ", end="")
		else:
			break
	print()