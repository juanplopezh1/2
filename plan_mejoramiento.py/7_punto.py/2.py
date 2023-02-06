def funcion(numero):
    contador = 0
    for i in range(2,numero):   
        if numero % i == 0:
            contador +=1
            print("divisor:", i)
    
    if contador > 0 :
        print("El número no es primo" )
    else:
        print("El número es primo")

        
funcion(19)