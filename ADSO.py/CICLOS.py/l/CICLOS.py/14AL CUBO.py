j = int(input("ingrese el numero de 3 cifras"))
while j >=100 and j<=999:
    numt = str(j)
    u= int(numt[0]) + int(numt[1]) + int(numt[2]) + int(numt[3])
    cubo = u + u
    print("la suma es->",u)
else:
    print("debe ingresar un numero de cifras")