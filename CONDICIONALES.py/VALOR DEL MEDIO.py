#Pedir 3 numeros e indicar cual de ellos es el valor del medio.
j = int(input("dijite el primer numero"))
u = int(input("dijite el segundo numero"))
a = int(input("dijite el tercero numero"))
menor=min( j , u , a )
mayor =max( j , u , a )
valor_medio =( j + u + a) - menor - mayor
print(menor, valor_medio, mayor)
print("el numero del medio es->",valor_medio)