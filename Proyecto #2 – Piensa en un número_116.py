import random
print(" Proyecto #2")
print(" Piensa en un número inversa de Adivina el número secreto ")
print(" *********Este numero debe estar entre 1 y 100************")
intentos = 0
adivinanza_minima = 1
adivinanza_maxima = 100
adivinanza_actual = 0
while True :
    intentos += 1
    if adivinanza_minima > adivinanza_maxima:
        print("DEBE SER SINCERO, INTENTE OTRA OPORTUNIDAD")
        print()
        break
    else:
        adivinanza_actual = random.randint(adivinanza_minima,adivinanza_maxima)

    print(f"¿Es {adivinanza_actual} tu numero?: ")
    respuesta = input("Ingresa: 'mayor', 'menor','correcto': ").lower()

    try:
        if respuesta == "correcto":
            print(f"Adivine tu numero: {adivinanza_actual} en {intentos} intentos")
            break
        
        elif respuesta == 'mayor':
            adivinanza_minima = adivinanza_actual+1
        
        elif respuesta == 'menor':
            adivinanza_maxima = adivinanza_actual-1
        
        else:
            print("Respuesta no valida, intenta otravez ")

    except ValueError:
        print(f"Ingresa solo numero entero")
    except Exception:
        print(f"Error critico¡¡: {e}")
         
        



#    try:
#        adivinanza = int(input("ingresa tu adivinanza : "))
#
#        if adivinanza < numero_secreto:
#            print("El numero es mayor")
#        elif adivinanza > numero_secreto:
#            print("El numero es menor")
#        else:
#            print(f"!FELICIDADES HAS ADIVIDANO EL NUMERO SECRETO: {(numero_secreto)} en: {intento} intentos")
#            print()
#            print()
#            break
#    except ValueError:
#        print(f"Ingresa solo numero entero")
#    except Exception:
#        print(f"Ingresa solo numero entero: {e}")
        

        

