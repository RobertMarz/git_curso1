print()
print("  PROGRAMA ORDENAMIENTO TUPLAS_98*")
print("Ejercicio suma tuplas tupla_de_tupla_98 *")
print("*************************/n")

tupla_de_tupla = (('Eduardo',26),('Maria',30),('Gerardo',20),('Valentina',22))
print()
personas = list(tupla_de_tupla)
print(f"Tupla: {tupla_de_tupla}")
print(f"Lista: {personas}")

longitud_lista = len(personas )
print(f"Nro de Elementos de la lista: -> {longitud_lista}")
for i in range(longitud_lista):
    for j in range(i+1,longitud_lista):

        if personas[i][1] > personas[j][1]:
            aux = personas[i]
            personas[i],personas[j] =personas[j],aux

print(f"La persona de menor edad es: {personas[0]}")
print(f"La persona de mayor edad es: {personas[-1]}")   

