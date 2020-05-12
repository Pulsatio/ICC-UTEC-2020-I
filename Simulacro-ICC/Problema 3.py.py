L=int(input("Dime la longitud del lado: "))
while L<5 or L>10:
    print ("Valor invalido")
    L=int(input("Dime la longitud del lado: "))
contador=L
for Fila in range(1,L+1):
    for Columna in range(1,L+1):
        if Columna==1 or Fila==1 or Columna==L or Fila==L or Columna==Fila or Columna==contador:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    contador=contador-1
    print()







