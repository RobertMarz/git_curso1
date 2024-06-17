# en docs,python,org
#print(" La funcion import ")
# en docs,python,org
import math,random
print(f" la raiz cuadrada de 25 es : {math.sqrt(25)}")
print(f" El seno de 30 es : {math.sin(30)}")
# se puede usar alias como
import math as Mt
print(f" la raiz cuadrada de 25 es : {Mt.sqrt(25)}")
# para no importar todas las funciones de math hacemos asi:

from math import sqrt,sin
print(f" la raiz cuadrada de 25 es solo sqrt : {sqrt(25)}")

# from math import * importa todo pero no es recomendable !

print("Números aleatorios")
# from random import randint
num = random.randint(1,100)
print("Número entero aleatorio random.randint(1,100)",num)
numf = random.random()
print("Número float emtre (0.0,1.0) aleatoriorandom.random()",numf)
numR = random.randrange(0,100,2)
print("Número random.randrange(0,100,2) ",numR)





