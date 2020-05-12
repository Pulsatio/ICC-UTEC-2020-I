while 1:
	numero_notas = int(input("Ingrese el numero de notas: "))	
	if numero_notas>1 and numero_notas<=10:
		break
promedio,menor_nota,mayor_nota=0,10000,-1
for i in range(1,numero_notas+1):
	while 1:
		print("Ingrese la nota",i,": ",end="")
		nota = int(input())
		if nota>0 and nota<=20:
			break
	promedio+=nota
	if menor_nota>nota:
		menor_nota=nota
	if mayor_nota<nota:
		mayor_nota=nota
promedio/=numero_notas

print(promedio,",",menor_nota,",",mayor_nota) 
