print("* FUNCION format() y len()*")
print("************************\n")

nombre = "Robert Marziliano"
edad = 62
print("Hi {} tu tienes {} años de edad".format(nombre,edad))

print("metodo uno\n")

print("Hi {nombre} tu tienes {edad} años de edad".format(nombre="JUAN",edad= 62))
print("metodo DOS\n")

nombre1 = "Rulo "
edad1 = 63

print("Hi {0} tu tienes {1} años de edad".format(nombre1,edad1))

print("metodo TRES\n")

frase = "Meses: {1}, {0} y {2}".format('Enero','Febrero','Marzo')
print(frase)

print("\n************************")
print("* FUNCION LEN *")
print("************************\n")

print("Robert Marziliano tiene ",len("Robert Marziliano tiene "),"caracteres")