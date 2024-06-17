print(" Manejo de excepciones (try – except) ")
# encerramos el codigo donde se genera el error al igresar erroes 
# ValueError
try:
    numero = int(input("Ingresa un numero da error con cero: "))
    resultado =  50/ numero
    print(resultado)
except ValueError as ve:
    print(f"Ingresa solo numero entero error: {ve}")
    
try:
    numero = int(input("Ingresa un numero: "))
    resultado =  50/ numero
    print(resultado)
except Exception as ve:
    print(f"Solo puede ingresar enteros : {ve}")



