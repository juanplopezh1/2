#En un juego de preguntas a las que se responde “Si” o “No” gana quien responda correctamente las tres preguntas.
j = input(print('¿Colon descubrió América?'))
if j == 'Si':
    print('muy bien :correcto')
    u = input(print('¿La independencia de Colombia fue en el año 1810?'))
    if u == 'Si':
        print('muy bien :correcto')
        a = input(print('¿The Doors fue un grupo de rock Americano?'))
        if a == 'Si':
            print('muy bien: correcto')
            print('¡Felicitaciones, sos muy inteligente !')
        else:
            print('Respuesta incorrecta')
            print('juego acabado')
    else:
        print('Respuesta incorrecta')
        print('juego acabado')
else:
    print('Respuesta incorrecta')
    print('juego acabado')
