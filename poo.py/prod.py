class producto:
    def __init__(self,nombre,precio,iva):
        self.__nombre=nombre 
        self.__precio=precio
    
    def getnombre(self):
        return self.__nombre
    def setnombre(self,nombre):
        self.__nombre = nombre
    def getprecio(self):
        return self.__precio
    def setnombre(self,precio):
        self.__precio=precio 
    def getiva(self):
        return self.__iva
    def setiva(self,iva):
        self.__iva=iva
    def getcalculadora(self):
        a = self.__precio*self.__iva
        a /100 
        print("es",a)
        
        
        
        
pr=producto("arroz",1500,0.19)
print("el nombre del producto es",pr.getnombre())
print("el precio del producto es",pr.getprecio())
print("el precio con iva es : ",pr.getcalculadora)

        

        