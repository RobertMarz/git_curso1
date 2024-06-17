print("\n************************")
print("*  MODIFICANDO INSERTAR Y ELIMINAR ELE DE LISTA pop,remove y del  *")
print("************************\n")

print("Lista Homogeneas \n")
vocales = ["a","e","i","o","u"]
print(vocales)
vocales.insert(2,"x")
print(vocales)
vocales.insert(8,"x")
print(vocales)
print("ELIMINAR varios \n")
vocales = ["a","e","i","o","u"]
vocales.pop(0)
print(vocales)
print("ELIMINAR con removed() la i uno solo \n")
vocales = ["a","e","i","o","u","i"]
vocales.remove("i")
print(vocales)
print("ELIMINAR con del a \n")
del vocales[0]
print(vocales)
print("usando f")
vocales = ["a","e","i","o","u"]
del vocales[1]
print(f"Eliminemos la e asi queda {vocales}")
print("ELIMINAR RANGO 0 3usando f")
del vocales[0:3]
print(f"Eliminemos RANGO {vocales}")
vocales = ["a","e","i","o","u"]
del vocales[:]
print(f"Eliminemos TODO queda NADA {vocales}")
