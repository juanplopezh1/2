#escriba si son los tres iguales, si hay dos iguales o si son los tres distintos
print ('Escriba el primer numero: ')
j=int(input())
print ('Escriba el segundo numero: ')
u=int(input())
print ('Escriba el tercer numero: ')
a=int(input())
if j==u==a:
    print ('Los tres numeros son iguales')
elif j==u or j==a or u==a:
    print ('Hay dos numeros iguales')
else:
    print ('Los tres numeros son distintos')