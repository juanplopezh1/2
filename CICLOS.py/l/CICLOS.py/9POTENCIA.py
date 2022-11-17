#Calcular la operación x n sin utilizar la función pow
j = int(input("Ponga la base: "))
u = int(input("Ponga el exponente: "))
a = 1
n = j

while(a < u):
    a+=1
    n*=j
if u <= 0:
    n=1
print(n)