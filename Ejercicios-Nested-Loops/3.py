N = int(input("n: "))

for j in range(N):
	for i in range(N):
		if i==0 or j==0 or\
		i==N-1 or j==N-1:
			print(j+1, end="")
		else:
			print(" ", end="")
	print()