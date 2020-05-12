N = int(input("Ingrese el numero de pacientes: "))

for i in range(N):
	name = input("Ingrese el nombre: ")
	age = int(input("Ingrese la edad: "))
	if age <= 2:
		age *= 10.5
	else:
		age -= 2
		age = age*4 + 21.0
	print("La edad de " + name + " es " + str(age))
	
