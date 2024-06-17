
print("\n************************")
print("* FUNCION fstring strip lstrip rstrip istitle() y title()  *")
print("************************\n")

print(f"EL RESULTADO DE 4+1 = {4+1}\n")

nombre = "Robert"
Estatura = 1.78
Edad = 62

print(f"Tu nombre es: {nombre}, tu estatura: {Estatura} y tu edad: {Edad}\n")

print("Ejemplo 3\n")

nombre = input("Ingrese su nombre : ")
num1 = int(input("Ingrese un numero : "))
num2 = int(input("Ingrese otro numero : "))

print(f"Hola {nombre} el resultado de {num1} + {num2} es :{num1 + num2} ")
print("() * FUNCION strip lstrip rstrip/* ()* ")
cadena = "() * FUNCION strip lstrip rstrip/* ()* "
cadena = cadena.strip() #quita " " de la derecha
print(cadena)
cadena = cadena.strip("*") #quita "*" de la derecha
print("de cadena.strip() ->",cadena)
cadena = cadena.strip("()") #quita "()" de la derecha
print(cadena)
cadena = cadena.rstrip(" /") #quita "/" de la derecha
print(cadena)

print("\n************************")
print("* FUNCION istitle() *")
print("************************\n")

print("roBert marziliAno\n")
cadena = "roBert marziliAno"
cadena = cadena.istitle() # falso si no es toda mayuscula
print(cadena)
#___________________________________________________
print("Robert Marziliano\n")
cadena = "Robert Marziliano"

cadena = cadena.istitle() # true si la primera es mayuscula
print(cadena)
name1 = input("Ingrese Nombre : ")
Apellido = input("Ingrese Apellido : ")
full_name = f"{name1} {Apellido}"
print()
print(f"{full_name}")
print(f"El formato istitle se aplico?: {full_name.istitle()}")
print(f" aplicando title : {full_name.title()}")
print(f" Original : {full_name}")
