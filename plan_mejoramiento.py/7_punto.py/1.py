#cuantas veces ocurre la linea de codigo 4
def funcion(tam,div):
    for i in range(1,tam):
        if(i%div==0):
            print(i,"es multiplo de ",div)
        else:
            print(i,"no es multiplo de",div)

funcion(100,10)
#porwue comienza a contar desde 0 y se cumple 10 veces entonces hasta el 9

