N = int(input("Ingrese un número: "))
for j in range(N):
	for i in range(2*N-1):
		if i<N-1:
			num = j-(N-2-i)
			if  num > 0:
				print(num, end="")
			else:
				print(" ", end="")

		if i==N-1:
			if j==0:
				print(1, end="")
			else:
				print(" ", end="")

		if i>N-1:
			num = j-(i-N)
			if  num > 0:
				print(num, end="")
			else:
				print(" ", end="")


	print()
