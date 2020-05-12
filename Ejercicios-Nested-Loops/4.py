texto = input("Texto: ")

par = ""
impar = ""
for i in range(len(texto)):
	if i%2 == 0:
		par+= texto[i]
	else:
		impar+= texto[i]

print("Par: ",par)
print("Impar: ",impar)