print("  PROGRAMA CON TUPLAS_95*")
print("Ejercicio suma tuplas_97 *")
print("*************************/n")

print("Ejercicio 1suma tuplas ")
tupla1 = [1,2,3,4,5]
tupla2 = [8,6,4,2,0]
print(f"tupla1:  {tupla1}")
print(f"tupla1:  {tupla2}")
# hacem0s una lista vacia
add_tupla = []
# podemos hacerlo con for y range(tupla1) pero 
# lo haremos con zip() unio de tuplas
# OJO LO UNIMOS CON zip y luego lo convertimos a lista crear la tupla unida
print(f"union de tuplas con zip  {list(zip(tupla1,tupla2))}")
for x,y in list(zip(tupla1,tupla2)):
    add_tupla.append(x+y) 

print()
print(f"tupla1:  {tupla1}")
print("+")
print(f"tupla2:  {tupla2}")
print("          **********************")
print(f"  Suma:  {add_tupla}")
    

