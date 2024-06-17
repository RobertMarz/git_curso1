print("**************************************************")
print("* Sistema dterminar si un numero es par  o impar *")
print("**************************************************\n")

numero =int( input("Ingrese el numero: "))

if numero % 2 == 0: # Uso de % devuelve el resto
    print('El numero: ',numero, 'Es Par')

elif numero % 2 == 1:
    print('El numero: ',numero, 'Es Impar')
print('Fin ')    

  
print("*******************************************")
print("* Sistema Cual es el numero mayor de tres *")
print("*****************************************\n")

uno =int( input("Ingrese el primer numero: "))
dos =int( input("Ingrese el primer numero: "))
tres =int( input("Ingrese el primer numero: "))


if uno > dos and uno > tres:
    print("El numero : ",uno,"Es el Mayor de los tres")
elif dos > tres:
    print("El numero : ",dos,"Es el Mayor de los tres")
else:
    print("El numero : ",tres,"Es el Mayor de los tres")
print('Fin ')    

