#Pida un numero al usuario que representa días del año.
j = int(input('Ingrese un número que será convertido a el día que corresponde del año'))
if j <= 31:
    print('Es el',j, 'de enero')
elif j <= 59:
    f = j - 31
    print('Es el',f, 'de febrero')
elif j <= 90:
    m = j - 59
    print('Es el',m, 'de marzo')
elif j <= 121:
    a = j - 90
    print('Es el',a, 'de abril')
elif j <= 152:
    ma = j - 121
    print('Es el',ma, 'de mayo')   
elif j <= 182:
    jun = j - 152
    print('Es el',jun, 'de junio')
elif j <= 213:
    ju = j - 182
    print('Es el',ju, 'de julio')
elif j <= 244:
    ag = j - 213
    print('Es el',ag, 'de agosto')
elif j <= 274:
    s = j - 244
    print('Es el',s, 'de septiembre')
elif j <= 305:
    o = j - 274
    print('Es el',o, 'de octubre')
elif j <= 335:
    n = j - 305
    print('Es el',n, 'de noviembre')
elif j <= 366:
    di = j - 335
    print('Es el',di, 'de diciembre')
else:
    print('El número está fuera de rango')