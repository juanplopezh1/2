def funcion (juan,lau,manchas):
    if juan>lau<manchas:
        print("descendente")
    elif lau<juan>manchas:
        print("ascendente")
    else:
        print("iguales")
juan=4400 
lau=300
manchas=100
funcion(juan,lau,manchas)

#es acendente porque lau tiene menos que juan y mas que manchas por lo cual se cumpliria