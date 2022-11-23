#Escribir un programa que almacene la cadena de caracteres contraseña en una variable
j = "contraseña"
password = input("Introduce la contraseña: ")
if j == password.lower():
    print("La contaseña coincide")
else:
    print("La contraseña no coincide")