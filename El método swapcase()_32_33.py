print("\n************************")
print("*  Los métodos  El método swapcase() y capitalize()  *")
print("************************\n")

string = input("Intoduce un string : ")
print(f"\n invierte las letras a minusculas {string.swapcase()}")

#___________________________________________________
string = input("Intoduce otro string : ")
print(f"\n todas las letras a mayusculas : {string.capitalize()}")
# SO CONVIERTE LA PRIMERA A MAYUSCULAS Y EL RESTO A MINUSCULAS

str = "robertico"
print("el ejemplo es:", str)

print(str.upper()) # convierte a mayúsculas
print(str.lower()) # convierte a minúsculas
print(str.title()) # convierte a mayúsculas la primera letra de cada palabra
#print(str.count(substring [, inicio, fin])) # devuelve el número de veces que aparece el su\
#5 bstring en el string. Opcionalmente se puede indicar el inicio y fin.
#print(str.find(‘o’)) # devuelve el índice de la primera aparición de 'd' (o -1 si no lo enc\
#print(substr("ob") in str # devuelve True si el string contiene el substring
#print(str.replace("o", "A",count())) # reemplaza 'old' por 'new'un máximo de 'count' ve 10 ces (opcional).
#print(str.isnumeric()) # devuelve True si str contiene solamente números