#Telefónica realiza los cálculos del costo de una llamada de teléfono
j = 200
u = int(input('Ingrese los minutos que druó de la llamada'))
if u <= 3:
    print('La llamada de fue de',u, 'minutos, por lo cual el pago será de',j)
else:
    a = u-3
    n = (a*50) + j
    print('La llamada de fue de',u, 'minutos, por lo cual el pago será de',n)