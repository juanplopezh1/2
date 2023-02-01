import funciones 
n1 =int(input("ingrese un numero: "))
n2=int(input("ingrese el segundo numero: "))
print(";;operaciones matematicas ::")
print("""
1- sumar
2-restar
3-multiplicar
4-dividir
5-potencia""")
opccion=int(input("ingrese la operacion deseada: "))
if opccion==1:
    print(funciones.sumar(n1,n2))
elif opccion ==2:
    print(funciones.restar(n1,n2))
if opccion==3:
    print(funciones.multiplicar(n1,n2))
elif opccion==4:
    print(funciones.dividir(n1,n2))
if opccion==5:
    print(funciones.potencia(n1,n2))

else: print("el numero no es valido ")
