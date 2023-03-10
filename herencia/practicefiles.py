from Aprendiz import *                        #importamos la clase aprendiz 
from Curso import *                           #importamos la clase curso  

ap=Aprendiz('2560664A','Diego Suarez',123456) #hacemos una variable ap = la clase importada aprendiz y en el parametro los datos de la clase que deseamos
c1=Curso('Python Intermedio',200)             #hacemos una variable c1 = la clase importada curso  y en el parametro los datos de la clase que deseamos
c2=Curso('Python Avanzado',200)               #hacemos una variable c2 = la clase importada curso y en el parametro los datos de la clase que deseamos
#print(c1.getNombre())
ap.agregarCurso(c1)                           #ponemos la variable creada seguida de la funcion y en el parametro los datos deseados 
ap.agregarCurso(c2)                           #ponemos la variable creada seguida de la funcion y en el parametro los datos deseados 

for curso in ap.getCursos():                  #creamos un for en curso para que recorra todo el objeto 
    print(curso.getNombre())                  #imprimimos curso.getnombre 