print("Programa para calcular el promedio de notas de un alumno")
nombre = input("Ingresa tu nombre: ")
matematicas = float(input(nombre + " Cual es tu calificacion en matematicas:  "))
quimica = float(input(nombre + " Cual es tu calificacion en quimica:  "))
biologia = float(input(nombre + " Cual es tu calificacion en biologia:  "))

promedio = (matematicas+quimica+biologia)/3
# promedio  = int(promedio)
if promedio >= 6:
    print('Felicidades '+nombre+'"Aprobastes" con un promedio de: ',promedio)
    print('Felicidades '+nombre+'"Aprobastes" con un promedio de: ',round(promedio,2))

else:
    print('Lo sentimos '+nombre+'"Reprobastes" con un promedio de: ',round(promedio,3))
print('Fin ')
