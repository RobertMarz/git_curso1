print("\n************************")
print("*  Los métodos startswith(), endswith() y substring   *")
print("************************")

string = "Diana se peina sola"
print("string Original :",string)
resultado = 0
starts_with = "Ejemplos con startswith()"
ends_with = "ejemplos con endswith()"

print(f"\n{starts_with.rjust(50, '=')}")

resultado = string.startswith("D")
print(f"\n{string} comienza con la subcadena D: {resultado}")

resultado = string.startswith("d")
print(f"\n{string} comienza con la subcadena d: {resultado}")

resultado = string.startswith("Diana")
print(f"\n{string} comienza con la subcadena D: {resultado}")

resultado = string.startswith("se",6)
print(f"\n{string} comienza con la subcadena se desde la posicion 6: {resultado}")

resultado = string.startswith("se",6,7)
print(f"\n{string} comienza con la subcadena se desde la posicion 6: {resultado}")

print(f"\n{ends_with.rjust(50, '=')}")
resultado = string.endswith("A")
print(f"\n{string} comienza con la subcadena D: {resultado}")
resultado = string.endswith("a")
print(f"\n{string} comienza con la subcadena D: {resultado}")
resultado = string.endswith("sola")
print(f"\n{string} comienza con la subcadena D: {resultado}")
resultado = string.endswith("sola",10)
print(f"\n{string} comienza con la subcadena D: {resultado}")



