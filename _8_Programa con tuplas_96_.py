print("  PROGRAMA CON TUPLAS_95*")
print("Ejercicio propuesto con tuplas_96 *")
print("*************************/n")

print("Ejercicio 1")
names_tupla = ["Ana","Gerardo","Maria","Carlos","Valentina"]
validator = 0
while validator == 0:
    number = int(input("Ingresa un numero entre 0 y 4: "))
    if 0<= number <= 4:
        print(f"El mpmbre es:  {names_tupla[number]}")
        validator = 1
    else:
        print("Error de numero, vuelva a intentarlo")

# OTRA MANERA
print("OTRA MANERA........./n")
number = 0
while 0<= number <= 4:
    number = int(input("Ingresa un numero entre 0 y 4: "))
    if 0<= number <= 4:
        print(f"El mpmbre es:  {names_tupla[number]}")
        number = 8
    else:
        print("Error de numero, vuelva a intentarlo")
        number = 0
    

