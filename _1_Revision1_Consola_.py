#Ejemplos simpes de codigo sin validacion-------------
print("======================")
print(" ¡¡Revision Inicial tipos de datos, funciones, type() ")
print("======================\n")
print("Hola mundo\n")
#suma simple-------------------------------------------
print("Esto es una suma")
Uno = 1
Dos = 2
Resultado = Uno+Dos
print(Resultado)

#funcion simple para el calculo area del Cuadrado y el Circulo------
pi = 3.1416

def cuadrado(lado): #Calcula el area del cuadrado a partir de su lado
    return lado ** 2


def circulo(radio): #Calcula el area del circulo dado el radio
    return pi * radio ** 2

print ("Area.cuadrado =", cuadrado(2))
print ("Area.circulo =", circulo(1))

#Entrada de datos simples sin validacion---------------------------
Palabra = input("Introduce una palabra: ")
num_int = int(input("Introduce un numero entero:  "))
num_float = float(input("Introduce un numero flotante:  "))
num_complex = complex(input("Introduce un numero complejo:  "))

print("String: ",Palabra)
print("entero: ",num_int)
print("flotante: ",num_float)
print("complejo: ",num_complex)
print("La variable 'edad' es de tipo: " + str(type(num_int))) #Ver tipo
Stop = input("PARALO AHI : ")
#Entrada de datos2 simples sin validacion---------------------------
nombre = input("Cual es tu nombre: ")
print("Hola "+nombre+" Realizaremos una suma")

num_uno = int(input("Introduce el 1er valor:  "))
num_dos = int(input("Introduce el 2do valor:  "))

resultado = num_uno + num_dos

print(nombre+ " El resultado de la suma es: ",resultado)

#Entrada de datos3 simples sin validacion---------------------------
print("Programa simple calcular el promedio de notas de un alumno")
nombre = input("Ingresa tu nombre: ")
matematicas = int(input(nombre + " Cual es tu calificacion en matematicas:  "))
quimica = int(input(nombre + " Cual es tu calificacion en quimica:  "))
biologia = int(input(nombre + " Cual es tu calificacion en biologia:  "))

promedio = (matematicas+quimica+biologia)/3
promedio  = int(promedio)
if promedio >= 6:
    print("Felicidades ", nombre , "Aprobastes con un promedio de : ", promedio)

print("Fin ")




