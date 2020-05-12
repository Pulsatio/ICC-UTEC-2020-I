a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
opcion = input("Ingrese la opcion: ")
if opcion=="a":
	print("El area del triangulo es",a*b/2)
elif opcion=="b":
	print("El promedio de los numeross es",(a+b)/2)
elif opcion=="c":
	if b!=0:
		print("La divison de los numeroe es",a/b)
	else:
		print("B no puede ser 0")
elif opcion=="d":
	print("El mayor numero es ",end="")
	if a<b:
		print(b)
	else:
		print(a)
else:
	print("Opcion invalida")
