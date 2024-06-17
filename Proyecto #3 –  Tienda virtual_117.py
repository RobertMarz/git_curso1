import random
print(" Proyecto #3  Tienda virtual  ")
print(" *********Este numero debe estar entre 1 y 100************")
catalogo = {"Camiseta":20,
            "Jeans":40,
            "zapatos":60,
            "Sombrero":10
            }

carrito = []
while True :
    print("/n Menu")
    print("1. Agregar productos al carrito")
    print("2. Ver carrito")
    print("3. Realizar el pago y salir")

    opcion= input("Seleccione una opcion")

    if opcion == "1":
        print("/n productos disónibles: ")
        [print(f"• {producto} &{precio}") for producto, precio in catalogo.items()]
        producto = input("ingrese el nombre del producto a agregar: ").title()
        if producto in catalogo:
            carrito.append(producto)
            print(f"Producto  {producto} agregado al carrito")

    elif opcion == "2":
        print("/n carrito")
        for producto in set(carrito): #se convierte a conjunto por si 400 camisetas
            cantidad = carrito.count(producto)
            precio_unitario = catalogo[producto]
            print(f"{cantidad} {producto} - ${precio_unitario} c/u ")

    elif opcion == "3":
        total_a_pagar = sum(catalogo[producto] for producto in carrito)
        print(f"total a pagar &{total_a_pagar}")
        #
        try:
            monto_pagado = float(input("Ingrese el monto a pagar: "))
            cambio = monto_pagado -total_a_pagar
            if cambio >= 0:
                mensaje_cambio = f"su cambio es: &{round(cambio)}" if cambio > 0 else f" Exacto no e requiere cambio"
                print(f"Gracias por su compra {mensaje_cambio}")
                break
            else:
                print("El monto ingresado es invalido")

        except Exception as e:
            print("Monto Invalido")
    else:
        print("La opcion no validad, corrija")

    
