#scribir un programa que pregunte por un número de teléfono con este formato en la consola y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
tel = input("Introduce un número de teléfono con el formato +xx-xxxxxxxxx-xx: ")
print('El número de teléfono es ', tel[4:-3])