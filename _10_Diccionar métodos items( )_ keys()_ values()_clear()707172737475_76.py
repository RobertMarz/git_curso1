print("\n************************")
print("*METODOS Diccionarios método items() keys()  values() fromkeys()  *")
print("************************\n")

print("METODOS Diccionarios items() para obtener claves y elementos_ Tuplas")
dictionary_ages = {"Juan":32,
                   "Robert":62,
                   "Tahis":55}
print(f" Diccionario de edades Normal {dictionary_ages}\n") 
print(f" Metodo items() ver tuplas: \n {dictionary_ages.items()}\n") 
print(f" Metodo items()con constructor list(): \n {list(dictionary_ages.items())}\n")

"""se usa list para poder trabajar con cada uno de los elementos del diccionario """

print("METODOS Diccionarios keys()  para obtener claves solamente ")
print(f" Metodo items() ver tuplas: \n {dictionary_ages.keys()}\n")
print(f" Metodo keys()con constructor list(): \n {list(dictionary_ages.keys())}\n")

print("METODOS Diccionarios values()  para obtener valores ")
print(f" Metodo items() ver tuplas: \n {dictionary_ages.values()}\n")
print(f" Metodo values()con constructor list(): \n {list(dictionary_ages.values())}\n")

print("METODOS limpiar Diccionarios clear() \n")
dictionary_ages.clear()
print(f" Diccionario limpiado con clear() :  {dictionary_ages}\n")

print("Añadir y Modificar  y copy elementos del diccionario)  si no esta lo añade\n")
dictionary_ages = {"Juan":32,
                   "Robert":62,
                   "Tahis":55}
dictionary_ages_copy = dictionary_ages.copy()
dictionary_ages["Robert"] = 32
dictionary_ages["Tahis"] = 55
print(f" Diccionario de edades Normal {dictionary_ages}\n")
print(f" Diccionario copia {dictionary_ages_copy}\n")

print("METODOS fromkeys() copia matrices , strings y asigna valores \n")
sequence = dictionary_ages_copy
value = 62
name_dic = dict.fromkeys(sequence,value)
print(f" Diccionario copia {name_dic}\n")
print("METODOS fromkeys() con strings  \n")
sequence = "ROBERT"
value = 62
name_dic = {}.fromkeys(sequence,value)
"""  o asi tambien     name_dic = {}.fromkeys("ROBERT",62)"""
print(f" Diccionario copia {name_dic}\n")

"""_summary_
    Método Acción
diccionario.keys() Devuelve todas las claves del diccionario
diccionario.values() Devuelve todos los valores del diccionario
diccionario.pop(clave[,<default>]) Elimina la clave del diccionario y devuelve
su valor asociado. Si no la encuentra y se
indica un valor por defecto, devuelve el
valor por defecto indicado.
diccionario.clear() Vacía el diccionario
clave in diccionario Devuelve True si el diccionario contiene la
clave o False en caso contrario.
valor in diccionario.values() Devuelve True si el diccionario contiene el
valor o False en caso contrario
"""












