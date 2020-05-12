N = int(input("n: "))

for j in range(N):
	for i in range(N):
		if i<=j:
			print((i+j+1)%2, end="")
		else:
			break
	print()