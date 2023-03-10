class Curso:                             #creamos una clase que se llama curso 
    def __init__(self,nombre,horas):     #creamos una funcion con el constructor y en el parametro los datos necesitados con self al principio 
        self.__nombre=nombre             #creamos una variable de instania le ponemos como valor el dato deseado en este caso nombre 
        self.__horas=horas               #creamos una variable de instania le ponemos como valor el dato deseado en este caso horas
    def getNombre(self):                 #hacemos una funcion con get nombre y en el parametro self 
        return self.__nombre             #retornamos a la variable de instancia 