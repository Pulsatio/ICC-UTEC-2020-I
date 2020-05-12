def suma(n=0):
	# parametro por defecto n=0
		# suma de pares hasta el n
		return (n//2)*(n//2 +1)
	else:
		# suma de impares hasta el n
		return  (n//2 +1)*(n//2 +1)

numero = int(input("Ingrese un numero: "))
print("Resultado:",suma(numero))		