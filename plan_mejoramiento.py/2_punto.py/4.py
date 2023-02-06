def funcion(diccionario1,diccionario2):
    if(len(diccionario1)>len(diccionario2)):
        return 'diccionario1 es mayor'
    elif(len(diccionario1)<len(diccionario2)):
        return 'diccionario2 es mayor'
    else:
        return 'son iguales'
diccionario1={"perro":"dog","gato":"cat"}
diccionario2={"conejo":"rabit","caballo":"hourse"}
print(funcion(diccionario1,diccionario2))
#la funcion leen hace que lea la cantidad de elementos por lo cual los 2 tienen la misma cantidad y se cumpliria el else