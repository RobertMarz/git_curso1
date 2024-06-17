print("  PROGRAMA CON TUPLAS_95*")
print("Ejercicio propuesto con tuplas *")
print("*************************/n")

print("Ejercicio 1")
naums_tupla = [5,8,3,3,1,6,2]
print(f" Tupla Original: {naums_tupla}")
Numero_de_Tupla =  int(input("Ingrese un numero de la Tupla: "))
naums_tupla =list(naums_tupla)
len_naums_tupla = len(naums_tupla) # Para recoorer la lista
print(f" Longitud de Tupla: {len_naums_tupla}")
for index in range(len_naums_tupla):
    if naums_tupla[index] == Numero_de_Tupla:
        naums_tupla[index] = 0

naums_tupla = tuple(naums_tupla )
print(f" Tupla Modificada: {naums_tupla}")
        





























