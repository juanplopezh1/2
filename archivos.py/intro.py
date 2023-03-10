
flujo=open('archivos/inicio.txt','a')             #hacemos una variable en la cual vamos a dar igual y ponemos un metodo llamado open y en el parametro la ruta necesaria 
#datos=flujo.read()
#print(datos)
flujo.write('\nCuando estudian con juicio')       #ponemos la variable seguido de un punto y el write (hacemos un salto de linea y lo que deseamos escribir en el archivo de la ruta de arriba )
datos=flujo.read()                                #ponemos una variable. read que es para leer la ruta del archivo 
print(datos)                                      #imprimimos todo lo escrito en la variable datos 
