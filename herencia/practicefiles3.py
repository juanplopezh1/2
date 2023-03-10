nombre=input('ingrese nombre del aprendiz')                                           #creamos una variable y ponemos el input para ingesar un dato por teclado 
documento=int(input('ingrese documento del aprendiz'))                                #creamos una variable documento y ponemos un int para ingresar un valor entero 
ficha=input('ingrese ficha del aprendiz')                                             #creamos una variable ficha y el input para ingresar por teclado 
    
ap=Aprendiz(ficha,nombre,documento)                                                   #creamos una variable ap y ponemos la clase en los parametros ponemos los datos ingresados en la clase 

nombreCurso=input('ingrese nombre del curso')                                         #creamos una variable y ponemos un input para ingresa por teclado 
horas=int(input('ingrese intensidad horaria del curso'))                              #creamos una variable con int para ingrear un valor entero y input para ingresar un valor por teclado 
c1=Curso(nombreCurso,horas)
ap.agregarCurso(c1)                                                                   #creamos una variable c1 llamamos curso y un parametro con los datos

with open('herencia/aprendices.txt','a') as flujo:                                    #abrir la carpeta con la ubicacion 
     flujo.write(ap.getFicha()+','+ap.getNombre()+','+str(ap.getDocumento())+'\n')    #get ficha get nombre get documento los llamamos con la respectiva variable y separadas por coma 