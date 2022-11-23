#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido 
años = int(input("¿Cuántos años tienes? "))
for i in range(años):
    print("Has cumplido " + str(i+1) + " años")