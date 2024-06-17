print("Unión e Intersección de conjuntos – El método union() y intersection()  _102*")
print(" Diferencia de conjuntos – El método difference() ")
print("Diferencia Simétrica – El método symmetric_difference")
print("Agregar un elemento a un conjunto – El método add()")
print("Agregar elementos a un conjunto a la vez – El método update()")
print("Eliminar elementos de un conjunto – Métodos remove() y discard()")
print("***************************************************************/n")

conj_A = {"Luis","Diego","Andres","Carlos"}
conj_B = {14,21,"Luis"}
print(conj_A)
print(conj_B)
print(" U N I O N.........................")
print(f"conj_A.union(conj_B) =  {conj_A.union(conj_B)} ")
print(f"conj_A.union | conj_B =  {conj_A|conj_B} ")

#  intersection()
print(" I n t e r s e c c i ó n...........")
print(f"conj_A & conj_B =  {conj_A & conj_B} ")
print(f"conj_A.intersection(conj_B) =  {conj_A.intersection(conj_B)} ")
print("NOTA: SI NO HAY INTERSECCION ENVIA set() como vacio ")
#print(f"conj_A.union(conj_B) =  {conj_A|conj_B} ")
#  intersection()
print(" Diferencia de conjuntos...........")
print(f"conj_A - conj_B =  {conj_A - conj_B} ")
print(f"conj_A.difference(conj_B) =  {conj_A.difference(conj_B)} ")
#print("NOTA: lo que esta en A pero no esta en B ")
print(" Diferencia Simétrica.........................")
print(f"conj_A  ^ conj_B =  {conj_A  ^ conj_B} ")
print(f"conj_A.symmetric_difference(conj_B) =  {conj_A.symmetric_difference(conj_B)} ")

print(" Agregar un elemento a un conjunto – El método add()...............")
Frutas = {"Peras","Manzanas","Uvas"}
print(Frutas)
Frutas.add("Mango")
print(f"Frutas.add('Mango')  =  {Frutas} ")

print(" Agregar un elemento a un conjunto  la vez – El método update()...............")
print(" Agregar lista, diccionario, tuplas etc...")
Frutas = {"Peras","Manzanas"}
Otras_Frutas = ["Mango","nispero","Uvas"]
print(Frutas)
print("Lista",Otras_Frutas)
Frutas.update(Otras_Frutas)
print(f"Frutas.update(Otras_Frutas)  =  {Frutas} ")


print(" Eliminar elementos de un conjunto – Métodos remove() y discard())...............")
print(" remove() elimina un elemento que se sabe y discard() elimina varios")
print(Frutas)
Frutas = {"Peras","Manzanas","Uvas","nispero"}
Frutas.remove("Manzanas")  # un solo elemento da error si esta
print("con removed ",Frutas)          
Frutas.discard("Peras")  # varios no da error si no esta
print("con discard ",Frutas)
Frutas.discard("Peras")  # varios no da error si no esta
print("con discard ",Frutas)






































