print("\n************************")
print("*METODOS Diccionarios recorriendo con for    *")
print("************************\n")

print("recorriendo con for el Diccionarios \n")
""" usando setdefault() crea la clave y retorna el valor"""
Dic_Val = {"a":1,"b":2,"c":3,"d":99}
print(f" Aplicacion setdefault()   {Dic_Val}\n")

for key in Dic_Val:
    print(f" {key} :  de {Dic_Val}\n")

print("*EXTRAE LOS VALORES INDEPENDIENTES DEL DICC COMO TUPLAS*")
for key, value in Dic_Val.items():
    print(f" {key} : {value} de {Dic_Val}\n")

print("Dos formas de eliminar elementos del diccionario")
print("------------------------------------------------")
edades = {"Ane":22,"Jokin":27,"Aitor":15}
print(f"Dicc: Original: -> {edades}")
print("Eliminenmos del edades ['Aitor'] ")
del edades ["Aitor"]
print(f"Queda entonces: -> {edades}")

edades1 = {"Ane":22,"Jokin":27,"Aitor":15}
print(f"Dicc: Original: -> {edades1}")
print("Eliminenmos edades1.pop('Aitor')")
edades1.pop("Aitor")
print(f"Queda con pop entonces: -> {edades1}")

# EJERCICIO1 Crea una programa de Login que compruebe el usuario y contraseña en diccionario MAX 3 intentos
usuarios = {"iperurena": {"nombre": "Iñaki","apellido": "Perurena","password": "123123"},
            "fmuguruza": {"nombre": "Fermín","apellido": "Muguruza","password": "654321"},
            "aolaizola": {"nombre": "Aimar","apellido": "Olaizola","password": "123456"}
            }

#EJERCICIO2 Crea un programa para introducir a un profesor las notas de sus estudiantes (máximo 10 estud
estudiantes = {"1": {"nombre": "Lorea","nota": 8},
               "2": {"nombre": "Markel","nota": "4.2"},
               "3": {"nombre": "Julen","nota": 6.5}
               }