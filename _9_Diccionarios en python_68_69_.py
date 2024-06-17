print("\n************************")
print("*  IMPLEMENTACION DE DICCIONARIOS EN PYTHON*")
print("************************\n")

dictionary_empty = {}

print(f" Diccionario vacio {dictionary_empty}")
print()
# Diccionario homogeneo
dictionary_ages = {"Juan":32,
                   "Robert":62,
                   "Tahis":55}
print(f" Diccionario homogeneo de edades {dictionary_ages}") 
     
# Diccionario heterogeneo
dictionary_dates = {"name":"Robert",
                   "last_name":"Marziliano",
                   "age":62}
print(f" Diccionario heterogeneo {dictionary_dates}") 
     
# Diccionario puede almacenar listas
dictionary_list ={"a":{"a": 1},
                  "b": [0,1,2]
                  }
print(f" Diccionario con lista{dictionary_list}") 
print()
# Diccionario puede tener claves numericas
dictionary_keys_num ={4:1,
                      5:2,
                      6:3,
                      }
print(f" Diccionario con claves numericas {dictionary_keys_num}") 
print()
# Diccionario ejemplo de lo que no se debe hacer Juan
dictionary_ages = {"Juan":32,
                   "Robert":62,
                   "Juan":55}
print(f" Diccionario de edades {dictionary_ages}")
print()
# Diccionario puede tener claves distintas
dictionary_keys_num ={4:1,
                      "a":2,
                      6:["z",1,2,3,["Robert"]],
                      }
print(f" Diccionario con claves numericas {dictionary_keys_num}")
print()
print(f" Mostrar elementos por clave de 'a' {dictionary_keys_num['a']}")
print(f" Mostrar la lista de clave 6 {dictionary_keys_num[6]}")
print(f" Mostrar el elemt 4 de lista de  clave 6 {dictionary_keys_num[6][4]}")





















