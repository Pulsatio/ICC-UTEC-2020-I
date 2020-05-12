A=int(input("Dime un número: "))
B=int(input("Dime otro número: "))
N=input("¿Qué opción deseas ejecutar?: ")
if N=="a":
    if A==0:
        print("Un triángulo no puede tener 0 como base")
    if B==0:
        print("Un triángulo no puede tener 0 como altura")
    else:
        area=round(A*B/2,3)
        print("El área del triángulo es",area)
elif N=="b":
    Promedio=round(A+B/2,3)
    print("El promedio de", A , "y", B ,"es",Promedio)
elif N=="c":
    if B==0:
        print("B no puede ser 0")
    else:
        División=round(A/B,3)
        print("La división de",A ,"y", B ,"es",División)
elif N=="d":
    if A>B:
        print("El número",A,"es mayor")
    if B>A:
        print("El número",B,"es mayor")
    if B==A:
        print("No hay número mayor")
