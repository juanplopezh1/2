class Persona:
    def __init__(self,identificacion):
    
        self.__identificacion=identificacion
            

    def getidentificacion(self):
        return self.__identificacion

    def setidentificacion(self,identificacion):
        self.__identificacion=identificacion

ob=Persona('juan')
print(ob.getidentificacion())
ob.setidentificacion('1014737953')
print(ob.getidentificacion())


class Aprendiz(Persona):
    def __init__(self,identificacion,ficha):
        Persona.__init__(self,identificacion)
        self.__ficha=ficha

    def getFicha(self):
        return self.__ficha

app=Aprendiz('ADSO',2560664)
print(app.getFicha())
print(app.getidentificacion())
