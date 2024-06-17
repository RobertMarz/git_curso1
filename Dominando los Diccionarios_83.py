print("\n************************")
print("*Dominando los Diccionarios en Python 5 Ejercicios Clav    *")
print("************************")

print("Ejercicios Nro 1 Diccionarios Nuros de manzanas? ")
""" usando setdefault() crea la clave y retorna el valor"""
fruits = {"manzanas":5,"peras":4,"naranjas":2}
print(f" Diccionario Original   {fruits}")
Nros_de_manzanas = fruits.get("manzanas")
print(f" Numero de manzanas es :   {Nros_de_manzanas}")
""" Otra forma"""
Nros_de_manzanas = fruits["manzanas"]
print(f" Numero de manzanas es :   {Nros_de_manzanas}")

print('Ejercicios Nro 2  Agregar 3 nuevos items con "bananas":5,"mangos":6,"uvas":3')
""" sin metodos """
fruits["bananas"] =5 
print(f" nuevo items sin metodo  {fruits}")
""" Otra forma"""
fruits.setdefault("mangos",5) 
print(f" nuevo items metodo setdefault  {fruits}")
""" Otra forma"""
fruits.update({"uvas":3}) 
print(f" nuevo items metodo update()  {fruits}")
print('Ejercicios Nro 3  eliminar el par clave valor con peras')
del fruits["peras"]
print(f" eliminado del dicc con metodo del.  {fruits}")
""" Otra forma"""
fruits.pop("naranjas")
print(f' eliminado "naranjas" con metodo pop()  {fruits}\n')

print('Ejercicios Nro 4  mostrar las claves solas y valores solos')
fruits = {"manzanas":5,"peras":4,"naranjas":2}
print(fruits)
keys_list = list(fruits.keys())
print(f' lista de claves con metodos list() y keys()  {keys_list}')
values_list = list(fruits.values())
print(f' lista de valores con metodos list() y keys()  {values_list}')

print('Ejercicios Nro 5 mostrar tru si manzanas existe y false si no')

if "manzanas" in fruits:
    print(f' "manzanas" Si esta en el dicc.  {fruits}')
else:
    print(f' "manzanas" No esta en el dicc.  {fruits}')
    



















