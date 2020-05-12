def es_primo(n):
	for i in range(0,n):
		if i*i>n:
			break
	# si tiene algun divisor no es primo
		if n%i==0:
			return False
	# si no tiene ningun divisor es primo
	return True
def es_mala_onda(n):
	while n%2==0:
		n/=2
	while n%3==0:
		n/=3
	while n%5==0:
		n/=5
	if n==1:
		return True
	else:
		return False
numero= int(input("Ingrese: "))
if es_mala_onda(numero):
	print(numero,"es mala onda")
else:
	print(numero,"no es mala onda")