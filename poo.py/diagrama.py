class lector:
    def __init__(self,nombre,direccion, telefono):
        self.__nombre=nombre 
        self.__direccion = direccion 
        self.__telefono = telefono 
    def getnombre (self):
        return self.__nombre 
    def getdireccion (self):
        return self.__direccion
    def gettelefono(self):
        return self.__telefono
    def setnombre(self,nombre):
        self.__nombre=nombre 
    def setdireccion (self,direccion):
        self.__direccion=direccion
    def settelefono(self,telefono):
        self.__telefono=telefono 
le = lector("juan lopez  :", "cll66a sur 71-4",3104096598)
print("el nombre del lector es :",le.getnombre())
print("la direccion del lector es :",le.getdireccion())
print("el numero del lector es :",le.gettelefono())




class pedido :
    def __init__(self,idusuario,tmaterial,cmaterial ):
        self.__idusuario=idusuario
        self.__tmaterial=tmaterial
        self.__cmaterial=cmaterial
    def getidusuario(self):
        return self.__idusuario
    def gettmaterial(self):
        return self.__tmaterial
    def getcmaterial(self):
        return self.__cmaterial
    def setidusuario(self,idusuario):
        self.__idusuario=idusuario
    def settmaterial(self,tmaterial):
        self.__tmaterial=tmaterial
    def setcmaterial(self,cmaterial):
        self.__cmaterial=cmaterial
pe=pedido(433124,"la espera",383838)
print("el id del usuario asignado es  :",pe.getidusuario())
print("el titulo del material del pedido es :",pe.gettmaterial())
print("el codigo asignado del codigo del material es :",pe.getcmaterial())




class determinar:
    def __init__(self,nn,lr):
        self.__nn=nn
        self.__lr=lr
    def getnn(self):
        return self.__nn
    def getlr(self,lr):
        return self.__lr
    def sab (self,nn):
        if "D" in nn:
            print("docente ")
    def doc (self,nn):
        if "E" in nn:
            print("estudiante ")
    def libro(self,lr):
        if "1" in lr:
            print("escogiste libro ")
    def revista(self,lr):
        if "2" in lr:
            print("escogiste revista ")
    
            
nn=input("ingrese D si eres docente : ingrese E si eres estudiante :")
lr=input("ingrese la opccion 1 si desdea libro ingrese la opccion 2 si desea revista  ")
det=determinar(nn,lr)
det.sab(nn)
det.doc(nn)
det.libro(lr)
det.revista(lr)
            
            
            
            
            
            
            
            
class revista :
    
      
 def __init__(self, revista ):
    self.__revista=revista
def getrevista(self):
    return self.__revista
def setrevista(self,revista):
    self.__revista=revista


class libro  :
    
      
 def __init__(self,libro,tlibro,tipolibro,autor,editorial ):
    self.__libro =libro
    self.__tlibro=tlibro
    self.__tipolibro=tipolibro
    self.__autor=autor
    self.__editorial=editorial  

def getlibro(self):
    return self.__libro 
def gettlibro(self):
    return self.__tlibro
def gettipolibro(self):
    return self.__tipolibro
def getautor(self):
    return self.__autor
def geteditorial(self):
    return self.__editorial
def setlibro(self,libro):
    self.__libro=libro
def settlibro(self,tlibro):
    self.__tlibro=tlibro
def settipolibro(self,tipolibro):
    self.__tipolibro=tipolibro
def setautor(self,autor):
    self.__autor=autor
def seteditorial(self,editorial):
    self.__editorial=editorial
    
li=libro("soledad","depresion extrema","sad","jisus","libros.e")
print("el nombre del libro es : ",li.getlibro())
print("el titulo  del libro es :",li.gettlibro())
print("el tipo de libro es :",li.gettipolibro())
print("el autor del libro es :",li.getautor())
print("la editorial del libro es :",li.geteditorial())
    


