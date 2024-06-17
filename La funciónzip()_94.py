print("           La función zip()_94*")
print("Agrupa o combinas listas diccionarios en pares como tuplas *")
print("***************************************************************/n")

print("Ejemplo 1")
names_tupla = ("Luis","Diego","Andres","Carlos")
ages_lista = [14,21,36,63,43]

combinacion = list(zip(names_tupla,ages_lista))
print("Ejemplo de zip unio de tupla mas lista:")
""" print(combinacion) hay que convertirlo a lista o tupla porque sino te da es la direccion donde esta """
print(f" como lista list(zip(names_tupla,ages_lista)): {combinacion}")
print("Ejemplo 2 usando for como se genera las tuplas")

for name,ages in zip(names_tupla,ages_lista):
   print(name,ages) 




























