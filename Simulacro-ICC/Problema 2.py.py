n=int(input("¿Cuántas notas va a ingresar?: "))
contador=0
Mayor=0
Menor=0
while n<=0 or n>10:
    n=int(input("¿Cuantas notas vas a ingresar?: "))
else:
    for i in range (n):
        m=int(input("¿Cuáles son las notas?: "))
        while 20<m or m<0:
            print("Nota no valida")
            m=int(input("¿Cuále son las notas?: "))
        else:
            contador=contador+m
            if i==0:
                Mayor=m
                Menor=m
            if Mayor>m:
                Mayor=m
            elif Menor<m:
                Menor=m
print("El promedio de las", n, "notas es: ",round(contador/n,4))
print("La nota mayor fue:",Mayor)
print("La nota menor fue:",Menor)






