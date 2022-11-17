j = int(input("Introducir dato maximo: "))
u= 0
contador = 0
centi = True
a = 0

while(a < j):
    u+=1
    a = 0
    for i in range(0, u+1):
        a+=i

print(u, "es el numero natural minimo solicitado para superar el dato maximo")