print("==============================================")
print("¡¡Programa para numero a palabra y viceversa!!")
print("=============================================\n")

print("Menu de Opciones\n")
print('Presiona 1 para convertir numero a palabra')
print('Presiona 2 para convertir palabra a numero')

Opcion = int(input("cual es tu opcion deseada: "))

if Opcion == 1:
    print('\n"conversor de numero a palabra"\n')
    Opcion_uno =int( input("cual es el numero que deseas convertir: "))
    if Opcion_uno == 1:
        print('"El numero es UNO": ')
    elif Opcion_uno == 2:
        print('"El numero es DOS": ')    
    elif Opcion_uno == 3:
        print('"El numero es TRES": ') 
    elif Opcion_uno == 4:
        print('"El numero es CUATRO": ')
    elif Opcion_uno == 5:
        print('"El numero es CINCO": ')    
    else:
        print('ESTA RUTINA SOLO PUEDE CONVERTIR HASTA 5')
elif Opcion == 2:
    print('\n"conversor de palabra a numero"\n')
    Opcion_dos = input("cual es la palabra que deseas convertir: ")
    Opcion_dos = Opcion_dos.lower()
    if Opcion_dos == "uno":
        print('"El numero es ": 1')
    elif Opcion_dos == "dos":
        print('"El numero es ": 2')    
    elif Opcion_dos == "tres":
        print('"El numero es ": 3') 
    elif Opcion_dos == "cuatro":
        print('"El numero es ": 4')
    elif Opcion_dos == "cinco":
        print('"El numero es ": 5')    
    else:
        print('EL NUMERO QUE INGRESO NO ESTA REGISTRADO')
else:
    print('Opcion no disponible')
print('Fin ')


