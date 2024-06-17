print()
print(" Superconjuntos issuperset()  Conjuntos y Subconjuntos – El método issubset( – La función set()_99 no puede tener listas, tuplas ")
# los elementos ser inmutables no puede tener listas, tuplas
print("*************************/n")
conjunto = {} # correcto
conjunto = {"elem","ele",1} # homogeneo o heterogeno
print(f"conjunto: {conjunto}")   
# se puede usasr la funcion set() para covertir objetos iterables a conjuntos
conjunto = set() # correcto
# correcto conjunto = set(objetos iterables)
conjunto = {1,2,5,4,3} # homogeneo
print(conjunto) # los acomoda el conjunto a su consideracion
conjunto = {"e","a"} # homogeneo
print(conjunto) # No los acomoda
#____________________________
# Esto seria un error conjunto = {1,{2,5},4,3} 
# homogeneo print(conjunto)
lista = ["a","c",1,4,9]
conjunto = set(lista)
subc_B = {"c",9}
print()
print(conjunto) # lo convierte
#  subconjunto metodo issubset()
print(f"subc_B = {"c",9} es subconjunto de conjunto: {subc_B.issubset(conjunto)}")

#  subconjunto estricto se usa con los operadores < o >
# Ejemplos
print(f"subc_B = {"c",9} < conjunto{"a","c",1,4,9}  {subc_B < conjunto}")
print(f"conjunto{"a","c",1,4,9}  < conjunto{"a","c",1,4,9}  {conjunto < conjunto}")
print(f"Pero Asi")
print(f"conjunto.issubset(conjunto: {conjunto.issubset(conjunto)}")
print("Superconjuntos___________________")
# issuperset() Superconjuntos contiene todos los elementos del subconjunto
superA = {"a","c",1,4,9}
subc_B = {"c",9}
print(f"superA es Superconjunto de subc_B {superA.issuperset(subc_B)}")
print(f"superA es Superconjunto > superA: {superA > superA}")

















