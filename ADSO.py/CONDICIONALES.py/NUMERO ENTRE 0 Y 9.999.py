#Pedir un número entre 0 y 9.999 y decir cuantas cifras tiene.
print("ingrese un numero entre 0 y 9.999 ")
j = int(input())
if(j<0 or j >9999):
    print("el numero ingresado es invalido")
else:
    if(j<10):
        print("el numero ingresado tiene 1 cifra")
    elif(j<100):
        print("el numero ingresado tiene 2 cifras")
    elif(j<1000):
        print("el numero ingressado tiene 3 cifras")
    elif(j<10000):
        print("el numero ingresado tiene 4 cifras")