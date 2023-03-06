class Persona:                                     #se crea una clase llamada persona
    def __init__(self,nombre):                     #definimos y ponemos el constructor paraque este se active                                     
        self.__nombre=nombre                       #aca le damos como valor el nombre que pusimos en el parametro y se activaria el constructor
        #print('Constructor Activado')        

    def getNombre(self):                           #aca definimos el nombre que recolectamos arriba y ponemos en el parametro self 
        return self.__nombre                       #retornamos y nos devolvemos a nombre 

    def setNombre(self,nombre):                    #definimos  nombre ya recolectado arriba y ponemos un parametro en el cual va a ir self y  nombre 
        self.__nombre=nombre                       #ponemos el constructor construido y le damos igual al nombre

ob=Persona('Maria')                                #llamamos a la clade persona y ponemos el parametro que deseamos imprimiir en este caso un nombre
print(ob.getNombre())                              #imprimimos la linea de arriba 
ob.setNombre('Ana')                                ##llamamos a la clade persona y ponemos el parametro que deseamos imprimiir en este caso un nombre
print(ob.getNombre())                              #imprimimos la linea de arriba 
#print(type(ob))

class Aprendiz(Persona):                           #creamos una clase llamada aprendiz y en el parametro ponemos la clase anteriorm,ente creada lo cual es persona 
    def __init__(self,nombre,ficha):               #definimos y le damos creacion al constructor y en el parametro ponemos self nombre y ficha 
        Persona.__init__(self,nombre)              #llamamos la clase creada y activamos el constructor y en el parametro self y nombre 
        self.__ficha=ficha                         #ponemos el constructor creado y le damos igual a la ficha 

    def getFicha(self):                            #definimos el recolectado arriba que seria ficha en este caso definimos y seria getficha y en el parametro self
        return self.__ficha                        #reornariamos self.__ficha

app=Aprendiz('Pedro',12345)                        #llamamos la clase de aprendiz y en el parametro lo deseado 
print(app.getFicha())                              #imprimimos la linea de arriba escrita ficha 
print(app.getNombre())                             ##imprimimos la linea de arriba escrita nombre 