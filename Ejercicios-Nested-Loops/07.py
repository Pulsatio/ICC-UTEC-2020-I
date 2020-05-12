n = 0
sum = 0
while n >= 0:
	n = int(input("Ingrese un numero: "))
	if not(n % 4) or not(n % 3): 	
		sum += n	
print("Suma:", sum)	
