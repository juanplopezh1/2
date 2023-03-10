class Persona:                                  #creamos una clase llamada persona 
    def __init__(self,nombre,documento):        #creamos una funcion con un contructor y en los parametros los datos deseados de primeras siempre self 
        self.__nombre=nombre                    #creamos una variable de instania le ponemos como valor el dato deseado en este caso nombre
        self.__documento=documento              ##creamos una variable de instania le ponemos como valor el dato deseado en este caso documento 
    def getNombre(self):                        #creamos una funcion getnombre  y en el parametro self 
        return self.__nombre                    #retornamos a la variable de instancia 
    def getDocumento(self):                     #creamos una funcion de get documento y en el parametro self 
        return self.__documento                 #retornamos a la variable de instancia 
    def setNombre(self,nombre):                 #hacemos una funcion lllamada setnombre y en el parametro self y nombre 
        self.__nombre=nombre                    #creamos una variable de instania le ponemos como valor el dato deseado en este caso nombre
    def setDocumento(self,documento):           #creamos una funcion setdocumento con un parametro  en el que va a ir self y el documento 
        self.__documento=documento              ##creamos una variable de instania le ponemos como valor el dato deseado en este caso horas
