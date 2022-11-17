#Determinar si un número es o no es perfecto.
from re import I


j = 1
u = 0
a= 0
n = int(input("Ingrese el numero: "))

while (n > j):
    if n%j == 0:
        u = j
    j+= 1

for j in range(u + 1):
    a+=1

if n == a:
    print(n, "Es perfecto")
else:
    print(n, "No es perfecto")