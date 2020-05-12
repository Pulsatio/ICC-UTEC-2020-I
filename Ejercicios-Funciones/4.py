def factorial(n=10):
	respuesta=1
	for i in range(1,n+1):
		respuesta=respuesta*i
	return respuesta

numero = int(input("Input: "))
print("Output:",factorial(numero))