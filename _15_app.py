# app.py

# import _14_mundo  //una forma//
# from _14_mundo import *  //otra forma//
from mi_paquete.funciones_matematicas import calcular_factorial,frase
# co alias sumar as sum
from mi_paquete.funciones_matematicas import sumar as sum
from _14_mundo import adios_mundo, hola_mundo

# Llamada a la función
hola_mundo()

# Llamada a la función
adios_mundo()
print(f"Llamando una funcion de mi paquete: factorial de 5 {calcular_factorial(5)} ")
print(f"la Frase es importada de paque es: {frase}")
print(f"importada la suam con alisa 10+2 : {sum(10,2)}")
"""
Localización de los módulos
Al importar un módulo Python lo buscara en los siguientes directorios:
1. En el directorio actual.
2. En los directorios declarados en el PYTHONPATH 
(variable de entorno que contiene un listado de directorios)
3. En el directorio de instalación de Python por defecto (en UNIX normalmente ‘/usr/local/lib/python/’    
"""