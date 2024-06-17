print("   La función enumerate(), import _111-114*")
print("   Recorre la posicion de un objeto iterable y da un contador*")
print("***************************************************************/n")

print("   La función enumerate() puede usar 2 argumentos")
# enumerate(objeto iterable, start = 0) si no se coloca  start = 0 siempre esta asi
frutas = ["manzana","platano","uva","sandia"]
print(frutas)
print("Recorrido con for")
for posicion,frut in enumerate(frutas):
    print(f"posicion : {posicion} : {frut} ")

print("Recorrido con for con start = 1")
for posicion,frut in enumerate(frutas, start = 1):
    print(f"posicion : {posicion} : {frut} ")

# si requiero
enumerado = list(enumerate(frutas, start = 1))
print(enumerado)
print()
print(" La funcion import ")
# en docs,python,org




































