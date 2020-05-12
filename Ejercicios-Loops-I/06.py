for i in range(1, 1001):
	print("Ping"* (i % 6 == 0), end="")
	print("Pong"* (i % 7 == 0), end="")
	if not(i % 7 == 0 or i % 6 == 0):
		print(i, end=" ")
	print()
