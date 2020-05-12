# Declarar las variables necesarias
N = 0
promedio = 0
menor = 21
mayor = 0

# Iterar por cada numero de notas no valido
while(N <= 1 or N > 10):
    N = int(input("Ingrese el total de notas: "))

# Iterar por cada nota
for i in range(1, N + 1):
    
    nota = 0
    
    # Iterar por cada nota no valida
    while(nota < 1 or nota > 20):
        nota = int(input("Ingrese la nota " + str(i) + ": "))
    
    # Agregar nota al promedio
    promedio += nota

    # Calculo de la menor nota
    if nota < menor:
        menor = nota
    # Calculo de la mayor nota
    if nota > mayor:
        mayor = nota
    
print(promedio/N, ", ", menor, ", ", mayor)
