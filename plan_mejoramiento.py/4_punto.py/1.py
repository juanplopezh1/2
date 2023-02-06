#el codigo presentado imprime
def funcion(dictionary,key,value):
    if key not in dictionary.keys():
        dictionary[key] = value
        print(dictionary)
    else:
        print('existe')
di ={"gato":"cat","perro":"dog","caballo":"hourse"}
funcion(di,'conejo','rabbit')



