print("            La función tuple() y Concatenación de tuplas*")
print("Crear tuplas partiendo de objetos iterables *")
print("***************************************************************/n")

print("Ejemplo 1")
x= 10
y = 5
""" coordenada = tuple(x,y) NO SE PUEDE SOLO UN ARGUMENTO USA LISTA""" 
coordenada = tuple([x,y]) # ASI SI ES CORRECTO
print(coordenada)

print("Ejemplo 2")
Texto= "Robert"
tupla_de_String = tuple(Texto) # ASI SI ES CORRECTO
print(tupla_de_String)

print("Ejemplo 3 con diccionario solo creara las claves")
Numb_dict = {"Uno":1,"Dos":2,"Tres":3}
tupla_de_dict = tuple(Numb_dict) # ASI SI ES CORRECTO
print(tupla_de_dict)

print("Ejemplo 4 con diccionario con valores")
Numb_dict = {"Uno":1,"Dos":2,"Tres":3}
tupla_de_dict = tuple(Numb_dict.values()) # ASI SI ES CORRECTO
print(tupla_de_dict)
print()
print("Ejemplo 5 Concatenación de tuplas ")
tupla1 = (1,2,3)
tupla2 = (4,5,6)
print(tupla1)
print(tupla2)
Tupla_concatenada = tupla1+tupla2
print(Tupla_concatenada)
print("Ejemplo 6 Concatenación de tuplas2 dentro de tupla1  ")
tupla1 +=tupla2
print(tupla1)
print("Ejemplo 7 Concatenación de tuplas y lista ")
tupla1 = (1,"x",3)
lista = [4,"y",6]
Tupla_concat = tupla1+tuple(lista)
print(Tupla_concat)































