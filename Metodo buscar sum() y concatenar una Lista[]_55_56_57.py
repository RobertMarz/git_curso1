print("\n************************")
print("*  METODO  index() y cocatenacion extend() DE LISTAS y SUMA*")
print("************************\n")


vocales = ["a","e","i","o","u"]
print(f"Lista Original {vocales}")
vocales.index("a")
print(f"\n Posicion de busqueda {vocales.index("a")}")
print(f"\n Posicion de busqueda desde 1  {vocales.index("e",1)}")
print(f"\n Posicion de busqueda desde 2 a 4 {vocales.index("o",2,4)}")
print(f"\n Posicion de busqueda desde 2 para ver error {vocales.index("a",0)}")

invitados = ["Cao","Juan","Germa"]
amigos = ["Luis","Pedro"]
print(f"cocatenacion de {invitados} y {amigos}\n")
invitados.extend(amigos)
print(f"cocatenacion final es: {invitados} \n")
numeros = [10,20]
print(f"cocatenacion ejemplo con range: {numeros} \n")
numeros.extend(range(30,100,10))
print(f"cocatenacion final con range: {numeros} \n")
print("METODODE SUMA LISTAS  \n")
NUMEROS = [1,2,3,4,5]
print(f"La SUMA DE LA LISTA: {NUMEROS} ES: {sum(NUMEROS)} \n")
print(f"La SUMA CON 10 DE INICIO: {NUMEROS} ES: {sum(NUMEROS,10)} \n")
print(f"La SUMA CON -10 DE INICIO: {NUMEROS} ES: {sum(NUMEROS,10)} \n")
NUMEROS = [1,2,3,4,True]
print(f"La SUMA DE LA LISTA: {NUMEROS} ES: {sum(NUMEROS)} \n")
