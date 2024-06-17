print(" Proyecto #1")
import random
print(" Adivina el número secreto ")
print(" He Seleccionado un numero entre 1 y 100, Adivina cual es ")
numero_secreto = random.randint(1,100)
intentos_maximos = 10
adivinanza = 0

for intento in range(1,intentos_maximos+1):
    print(f"\n intentos : {intento}/{intentos_maximos}")
    try:
        adivinanza = int(input("ingresa tu adivinanza : "))

        if adivinanza < numero_secreto:
            print("El numero es mayor")
        elif adivinanza > numero_secreto:
            print("El numero es menor")
        else:
            print(f"!FELICIDADES HAS ADIVIDANO EL NUMERO SECRETO: {(numero_secreto)} en: {intento} intentos")
            print()
            print()
            break
    except ValueError:
        print(f"Ingresa solo numero entero")
    except Exception:
        print(f"Ingresa solo numero entero: {e}")
        
if adivinanza != numero_secreto:
    print(f"Lo sentimos no has adivinado sera en otra oportunidad, el numero sec. era: {(numero_secreto)}")
        

salir = input("Presione la tecla enter para salir..")        

