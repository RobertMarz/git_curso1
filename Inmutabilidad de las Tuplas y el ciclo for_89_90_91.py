print("           Como acceder a Elementos de Tuplas *")
print("Inmutabilidad de las Tuplas  y CICLO FOR  y desempaquetado *")
print("***************************************************************/n")

print("Inmutabilidad de las Tuplas CASO 1")
nums_tuplas = ('a','e','i','o','u')
print(nums_tuplas)
""" nums_tuplas[0] = 6 NO SE PUEDE HACER EN TUPLAS SOLO LISTAS """

print("Inmutabilidad de las Tuplas CASO 2")
nums_tuplas = ([1,2,3],{'UNO':1,'DOS':2} ,(3,2))
nums_tuplas[0][1] = 87
nums_tuplas[1]['DOS'] = 88
print(f"Esto si nums_tuplas[0][1] = 4 o nums_tuplas[1]['DOS'] = 88 : {nums_tuplas}")

print("CICLO FOR PARA RECORRER Tuplas CASO 3")

for elem_de_tuplas in nums_tuplas:
    print(elem_de_tuplas)

print(" desempaquetado de Tuplas con CICLO FOR ")

fruits_tuplas = ('001','Manzana','Roja'),('002','Pera','Verde')
print(fruits_tuplas)
for code,fruit,color in fruits_tuplas:
    print(f" La fruta: {fruit} tiene el codigo {code} y es de color {color} ")









