#Un obrero necesita calcular su salario semanal
j = int(input('Ingrese las horas de trabajo semanales del obrero'))
if j <= 40:
    u = j * 2600
    print('Las horas de trabajo semanales del obrero fueron',j, 'por lo cual el pago será de',u)
else:
    a = j-40
    n = (a*5000)+(40*2600)
    print('Las horas de trabajo semanales del obrero fueron',j, 'por lo cual el pago será de',n)