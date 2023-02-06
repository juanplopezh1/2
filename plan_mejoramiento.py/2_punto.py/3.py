def funcion(d1,d2):
    if(len(d1)>len(d2)):
        return 'diccionario1 es mayor'
    elif(len(d1)<len(d2)):
        return 'diccionario2 es mayor'
    else:
        return 'son iguales'
d1={"1":"2","3":"4"}
d2={"1000":"2000","3000":"4000","5000":"6000"}
print(funcion(d1,d2))

#diccionario 2 tiene mas elementos 