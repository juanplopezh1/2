#Pedir una nota de 0 a 10 y mostrarla de la forma: Insuficiente, Suficiente, Bien,etc.
print("ingrese una nota para verificar->")
j = int(input())
if(j >=0 and j < 5):
    print("su nota es insuficiente para poder pasar :reprobado")
elif(j==5):
    print("su nota es suficiente :aprobado")
elif(j>5 and j <=9):
    print("su nota esta bien:aprobado")
elif(j==10):
    print("su nota es exelente:super aprobado:p")
else:
    print("el valor ingresado no es permitido")