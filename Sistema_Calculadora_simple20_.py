print("\n************************")
print("* CALCULADORA SENCILLA *")
print("************************\n")
print("1. SUMA")
print("2. RESTA")
print("3. MULTIPLICACION")
print("4. DIVISION")
print("5. DIVISION ENTERA")
print("6. EXPONENTE")
print("7. MODULO O RESTO\n")

numero =int( input("Ingrese la opcion deseada: "))

if numero == 1:
    print('SUMA\n')
    numero =int( input("Ingrese un numero: "))
    numero +=int( input("Ingrese otro numero: "))
    print('La suma es: ',numero)
elif numero == 2:
    print('RESTA\n')
    numero =int( input("Ingrese un numero: "))
    numero -=int( input("Ingrese otro numero: "))
    print('La Resta es: ',numero)
elif numero == 3:
    print('MULTIPLICACION\n')
    numero =int( input("Ingrese un numero: "))
    numero *=int( input("Ingrese otro numero: "))
    print('La multiplicacion es: ',numero)
elif numero == 4:
    print('DIVICION\n')
    numero =int( input("Ingrese un numero: "))
    numero /=int( input("Ingrese otro numero: "))
    print('La division es: ',numero)
elif numero == 5:
    print('DIVISION ENTERA\n')
    numero =int( input("Ingrese un numero dividendo: "))
    numero //=int( input("Ingrese numero divisor: "))
    print('La division entera es: ',numero)
elif numero == 6:
    print('EXPONENTE\n')
    numero =int( input("Ingrese un numero base: "))
    numero **=int( input("Ingrese numero exponente: "))
    print('La la exponenciacion es: ',numero)
elif numero == 7:
    print('MODULO O RESTO\n')
    numero =int( input("Ingrese un numero dividendo: "))
    numero %=int( input("Ingrese numero divisor: "))
    print('el modulo es: ',numero)
else:
    print('Esta opcion no esta disponible')
print('Fin ')    

  

