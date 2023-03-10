from Persona import *                                              #importamos la clase persona con from import 
#from Curso import * ...en caso de composición
class Aprendiz(Persona):                                           #creamos una clase llamada aprendiz y en el parametro la clase importada 
    def __init__(self,ficha,nombre,documento):                     #creamos un contructor y en el parametro los datos deseados 
        Persona.__init__(self,nombre,documento)                    #creamos un constructor de la clase persona  y en el parametro los datos especificos de el 
        self.__ficha=ficha                                         #le damos ficha a las variables de instancia
        self.__cursos=[]                                           #le damos cursos  a las variables de instancia
    def getFicha(self):                                            #hacemos una funcion con get ficha y en el parametro ponemos un self 
        return self.__ficha                                        #retornamos a la variable de instancia 
    def setficha (self,ficha):                                     #creamos una funcion en setficha y en el parametros pojnemos self y ficha 
        self.__ficha=ficha                                         #le damos valores a las variables de instancia 
    def agregarCurso(self,curso):                                  #creamos una funcion de agregar curso y ponemos en el parametro self y curso 
        #c=Curso('python',120) 
        self.__cursos.append(curso)                                #en la variable de instancia agregamos curso con append
    def getCursos(self):                                           #creamos una funcion con getcursos(ponemos en el parametro self )
        return self.__cursos                                       #retornamos a la variable de instancia de self cursos 