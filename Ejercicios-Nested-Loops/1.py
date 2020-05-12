while True:
	N = int(input("Ingrese el valor de N:"))
	if N>=3:
		break
	else:
		print("N tiene que se mayor a 3!")

for y in range(N):
	for x in range(N):
		if x<=y:
			print("*", end="")
		else:
			break
	print()
