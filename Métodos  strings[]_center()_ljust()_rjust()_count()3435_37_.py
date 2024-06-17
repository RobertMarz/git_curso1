# Métodos  strings[]_center()_ljust()_rjust()_count() 
print("\n************************")
print("*  Los métodos strings[]   *")
print("**************************")
string = "ABCDEFGHIJK"
print("String Original: ",string)
resultado = string[0]
print(f"{string} substring en string[0]->  : {resultado}")
resultado = string[0:3]
print(f"{string} substring en  string[0:3]-> : {resultado}")
resultado = string[3:]
print(f"{string} substring en  string[3:]->: {resultado}")
resultado = string[:]
print(f"{string} substring en  string[:]-> : {resultado}")
resultado = string[1:6:2] #De la pos 1 a la pos 6 de 2 en 2 para buscar
print(f"{string} substring en  string[1:6:2]-> : {resultado}")
resultado = string[::3] #saltando de 2 en 2 para buscar
print(f"{string} substring en  string[::3]-> : {resultado}")

print("\n************************")
print("*  Los métodos center(), ljust() y rjust() count()   *")
print("************************\n")

string = "Robert"
print(string.center(20))# Centrado
print(string.ljust(20))# Ajustado a la izquierda
print(string.rjust(20))# Ajustado a la derecha
print("\n Metodos con caracter")
print(string.center(20,"="))# Centrado con caracteres
print(string.ljust(20,"l"))# Ajustado a la izquierda con caracteres
print(string.rjust(20,"r"))# Ajustado a la derecha con caracteres
string = "Roberto="
print()
print(string)
print(string.count("")) #9 desde cero como uno
print(string.count("o")) #cuantas o desde cero
print(string.count("o",3)) #cuantas o desde cero
print(string.count("o",3,5)) #cuantas o desde cero hasta 5
#___________________________________________________

print("\n************************")
print("*  Los métodos islower(), lower(), isupper() y upper() *")
print("************************\n")

string = input("Intoduce un string : ")
print(f"\n todas las letras a minusculas {string.islower()}")# valor booleano
string = string.lower()
print(f"\ntodas las letras a minusculas : {string}\n")
#___________________________________________________
string = input("Intoduce otro string : ")
print(f"\n todas las letras a mayusculas : {string.isupper()}")
string = string.upper()
print(f"\ntodas las letras a mayusculas : {string}")
