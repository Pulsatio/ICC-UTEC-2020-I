n = 0
while(n < 1):
	n = int(input("n: "))
print("1"*n)

for i in range(2, n):
	print(str(i)+" "*(n-2) + str(i))

print(str(n)*n)

