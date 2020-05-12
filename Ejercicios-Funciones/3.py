def suma_intervalos(lista,pos1,pos2):
	lista = lista.split(" ")
	# Recordar que la lista que tenemos es un string
	# que contiene a los numeros separados por espacios
	# split() es una funcion muy util, documentese si no la entiende
	suma=0
	# Segun el problema el primer numero tiene indice 1
	for i in range(pos1-1,pos2):
		# un string se cambia a int con la funcion int()
		suma+=int(lista[i])
	return suma


lista = input("Input: ")
pos1 = int(input("pos1: "))
pos2 = int(input("pos2: "))
print("Output:",suma_intervalos(lista,pos1,pos2))