n=str(input("Escribe un oración: "))
x=0
y=0
z=0
q=0
while len(n.split())<5:
    print("Oración demasiado corta para ser admitida")
    n=input("Escribe una oración: ")
else:
    for i in (n):
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
            z=z+1
        if i.isalpha():
            x=x+1
        if i==" ":
            y=y+1
print("La cantidad de caráteres es",x)
print("La cantidas de vocales es",z)
print("La cantidad de espacios es",y)
print("La cantidad de consonantes es",x-z)


