#ingresa un numero de 4 cifras e invertirlo
j =(input("ingrese el numero de nueve cifras:"))
for i in range (len(j)-1,-1,-1):
    print((j[i]),end=("-"))