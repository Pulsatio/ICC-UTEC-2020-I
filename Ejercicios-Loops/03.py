for i in range(1, 1001):
	print("Tic"* (i % 4 == 0), end="")
	print("Tac"* (i % 6 == 0), end="")
	if not(i % 4 == 0 or i % 6 == 0):
		print(i, end=" ")
	print()
