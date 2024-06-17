print("\n************************")
print("*  Breve Udo de Lista[]  *")
print("************************\n")

print("Lista[] vacia \n")
Lista_vacia = []
print(Lista_vacia)
print("\Lista Homogeneas \n")
vocales = ["a","e","i","o","u"]
print(vocales)
print("\numeros_enteros \n")
numeros_enteros = [1,2,3,4,5]
print(numeros_enteros)
print("\numeros_decimales \n")
numeros_dec = [1.3,2.3,3.11,4.0,5]
print(numeros_dec)
print("\numeros_booleanos \n")
numeros_boo = [True,False,True]
print(numeros_boo)
print("\Lista Heterogeneas \n")
Lista_Heterogeneas = ["Robert",62,True]
print(Lista_Heterogeneas)

print("\n************************")
print("*  ANIDAMIENTO DE LISTAS[][][] list() para convertir LISTAS *")
print("************************\n")

LISTA = ["NONO","NONA",["MAMA",["Armando","Robert"]]]

print(f"\n LISTA GENERAL LISTA: {LISTA}  ")

print(f"\n LISTA SUBLISTA LISTA[2]: {LISTA[2]}  ")

print(f"\n LISTA SUBLISTADEsUBLISTA LISTA[2][1]: {LISTA[2][1]}  ")

print(f"\n LISTA SUBLISTADEsUBLISTA UN ELEMENTO LISTA[2][1][1]: {LISTA[2][1][1]}  ")

print(f"\n LISTA SUBLISTADEsUBLISTA UN ELEMENTO LISTA[2][1][0]: {LISTA[2][1][0]}  ")
print()

print("\n************************")
print("*  recorriendo Listas[] con for  *")
print("************************\n")

marcas = ["Apple","Samsung","Xiaomi"]
print(f"\n CUANTOS ELEMENTOS :  {marcas}")
print(f"\n ELEMENTO 1 :  {marcas[0]}")

for ch in marcas[0]:
    print(ch)
    
    
for elemento in ['Python','JavaScript','JAVA']:
    print("Programo en ", elemento)