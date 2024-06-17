print("-Tuplas- su manejo igual que las listas se usa ()")
print("*************************************************/n")

nombre_tuplas = ()# TUPLA VACIA
print(f"Tupla vacia : {nombre_tuplas}")
""" O ASI """
nombre_tuplas = (3,2)# HOMOGENEA
print(f"Tupla HOMOGENEA : {nombre_tuplas}")
""" O ASI """
nombre_tuplas = (3,) # DE UN SOLO ELEMENTO
print(f"Tupla DE UN SOLO ELEMENTO : {nombre_tuplas}")
""" O ASI """
nombre_tuplas = (3,True,"hola",3.5) # HETEROGENEA
print(f"Tupla HETEROGENEA : {nombre_tuplas}")
""" O ASI """
nombre_tuplas = 3,True,"hola",3.5 # ES LO MISMO
print(f"Tupla HETEROGENEA caso 2 : {nombre_tuplas}")
""" O ASI """
nombre_tuplas = ([1,2,3],{"uno":1,"dos":2},(3,2))# PUEDE HABER LISTAS, DICCIONARIOS SE PUEDEN MODIFICAR LOS ELEMENTOS DE LAS LISTA PERO CAMBIAR
print(f"Tupla HETEROGENEA COMBINADA: {nombre_tuplas}")


print("           Como acceder a Elementos de Tuplas *")
print("1. Por Indices 2. Por Segmentacion 3. Desempaquetados de Tuplas *")
print("***************************************************************/n")

print("1. Por Indices.........Nombre_Tupla[Indice].")
tuplas_vocales = ('a','e','i','o','u')
print(f"Tupla ORIGINAL : {tuplas_vocales}")
print(f"Elemento de la posicion 2 es la : {tuplas_vocales[2]}")
print(f"Elemento de la posicion -1 es la : {tuplas_vocales[-1]}")

print("2. Por Segmentacion...........Nombre_Tupla[Inicio,final,Salto].")
tuplas_vocales = ('a','e','i','o','u')
print(f"Tupla ORIGINAL : {tuplas_vocales}")
print(f"Los Elementos que estan dentro de [0:2] es la : {tuplas_vocales[0:2]}")
print(f"Elemento del Segmento [-3:-1] es la : {tuplas_vocales[-3:-1]}")
print(f"Segmento con salto de dos [0:5:2] o asi[::2]  es la : {tuplas_vocales[0:5:2]}")
print(f"Segmento con salto de dos igual [::2]  es la : {tuplas_vocales[::2]}")

print("2. 3. Desempaquetados de Tuplas...var1,var2 = Nombre_Tupla[Inicio,final,Salto].")
tuplas_vocales = ('a','e','i','o','u')
V1,V2,V3= tuplas_vocales[:3]
print(f"Tupla ORIGINAL : {tuplas_vocales}")
print(f"Unpacking V1,V2,V3= tuplas_vocales[:3] : {V1,V2,V3}")
V1,V2,V3,V4= tuplas_vocales[0:4:1]
print(f"Elementos  Desempaquetados de [0:5:1] o asi[:4:1]  es la :  {V1,V2,V3,V4}")













