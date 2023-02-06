def funcion(l1,l2):
    if(len(l1)>len(l2)):
        return 'lista1 es mayor'
    elif(len(l1)<len(l2)):
        return 'lista2 es mayor'
    else:
        return 'son iguales'
l1=[1,2,3,4,5,6,7,8,9]
l2=[1000.2000,3000,4000,5000,6000,7000]
print(funcion(l1,l2))

#lista 1 es mayor porque tiene mas elementos