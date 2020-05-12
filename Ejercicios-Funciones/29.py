n_min = int(input("Ingrese min: "))
n_max = int(input("Ingrese max: "))

def es_perfect(num):
 sum = 0
 for i in range(1,num):
  if num%i==0:
   sum += i
 if sum == num:
  return True
 return False

def es_primo(num):
 if num==1:
  return False
 for i in range(2,num):
  if num%i==0 and i!=1:
   return False
 return True

no_output = True
for n in range(n_min, n_max):
 if es_perfect(n):
  print(n, end=" ")
  if no_output:
   no_output = False
 elif es_primo(n):
  print(n, end=" ")
  if no_output:
   no_output = False

if no_output == True:
 print("No hay numeros perfectos ni primos")