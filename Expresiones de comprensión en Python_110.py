print("  Sintaxis Expresiones de comprensión en Python_110*")
print("***************************************************************/n")

print(" Sintaxis para crear expresiones de comprensión en Python ....")
print("# [expresion for elemento in obj_iterable if condicion]")
print("hacer un programa que genere una lista en Python ")
print("que de los cuadrados de  0 al 9 con y sin expresiones de comprensión")
cuadrados = []
for x in range(10):
    if x%2 == 0:
        #cuadrados = x**2
        cuadrados.append(x**2)

print()
print("sin expresiones de comprensión")
print(cuadrados)

print()
print("Con expresiones de comprensión")    
# [expresion for elemento in obj_iterable if condicion]
cuadradosC = [x**2 for x in range(10) if x%2 == 0 ]
print()
print("Con expresiones de comprensión")
print(cuadradosC)

# Crear Diccionario con sintaxis de comprension a partir de
# una lista de tuplas ejemplo
personas =[("Robert",62),("Nena",55),("Elvia",58)]
diccionario = {nombre:edad for nombre,edad in personas}

print(diccionario)








































