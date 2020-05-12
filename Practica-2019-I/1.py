palabra = input("Ingrese: ")
es_palindromo=1
for i in range(0,len(palabra)//2+1):
	# caracteres a la misma distancia del centro
	if palabra[i]!=palabra[len(palabra)-1-i]:
		es_palindromo=0
if es_palindromo==1:
	print("True")
else:
	print("False")