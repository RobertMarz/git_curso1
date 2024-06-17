print("\n************************")
print("*METODOS Diccionarios método get()  popitem()   *")
print("************************\n")

print("METODOS Diccionarios get()")
dictionary_ages = {"Juan":32,
                   "Robert":62,
                   "Tahis":55}
print(f" Diccionario de edades Normal {dictionary_ages}\n") 
 
Edad_Persona = dictionary_ages.get("Juan")
print(f" La edad de  Juan es  {Edad_Persona}\n") 
Edad_Persona = dictionary_ages.get("Jua")
print(f" La edad de  Jua Devuelve None por no estar ->  {Edad_Persona}\n") 
Edad_Persona = dictionary_ages.get("Jua",100)
print(f" La edad de  Jua Devuelve 100 por no estar retorna el valor ->  {Edad_Persona}\n")

print("METODOS Diccionarios  popitem() elimina el ultimo item = a ultima tupla")

item = dictionary_ages.popitem()
print(f" Aplicacion depopitem()   {dictionary_ages}\n")
print(f" tupla o item retornado   {item}\n")

print("METODOS Diccionarios  pop() elimina la dupla de la clave dada")
Elemento = dictionary_ages.pop("Robert")
print(f" Aplicacion depopitem()   {Elemento}\n")
print(f" Diccionario Como queda{dictionary_ages}\n")

""" retorna valor por no encontrado """
Elemento = dictionary_ages.pop("Rober",45)
print(f" Aplicacion depopitem()   {Elemento}\n")
print(f" Diccionario Como queda{dictionary_ages}\n")

""" retorna un keyerror por no encontrado KeyError: 'Rober' """
#Elemento = dictionary_ages.pop("Rober")
#print(f" Aplicacion de pop()   {Elemento}\n")
#print(f" Diccionario Como queda{dictionary_ages}\n")

""" usando setdefault() crea la clave y retorna el valor"""
Dic_Val = {"a":1,"b":2,"c":3}
print(f" Aplicacion setdefault()   {Dic_Val}\n")
Return_Val = Dic_Val.setdefault("d",4)
print(f" Valor retornado   {Return_Val}\n")
print(f" Aplicacion setdefault()   {Dic_Val}\n")
""" otra forma  si encuentra la clave retorna el valor que tiene """
Return_Val = Dic_Val.setdefault("a",4)
print(f" Valor retornado   {Return_Val}\n")
print(f" Aplicacion setdefault()   {Dic_Val}\n")

""" usando update() para agregar si clave no existe elementos a un diccionario"""

Dic_Val.update({"a":100,"e":7,"f":9})
print(f" Aplicacion update() dos nuevo elementos  \n  {Dic_Val}\n")














