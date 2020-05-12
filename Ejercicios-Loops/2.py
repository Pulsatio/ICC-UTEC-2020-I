n = int(input())
if n<3:
	print("N es menor que 3. Error")
else:
	for i in range(0,n):
		if i==0 or i==n-1:
			print("*"*n)
		else:
			print("*"+" "*(n-2)+"*")