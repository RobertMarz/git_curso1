print("\n************************")
print("*  Constructor list() para convertir LISTAS *")
print("**************************")

print(range(0,100,10)) #no hace nada para verlos es como sigue:
NUMEROS = range(0,100,10)
print(NUMEROS)
print(f"\n Es Asi: {list(NUMEROS)}\n ó \n Asi:    {list(range(0,100,10))} ")

Nombre = "Marziliano"
print(f"\n Como string: {Nombre}\n ó Convertido a Lista: {list(Nombre)} ")
print()
Convertida = list(Nombre)
print(Convertida[1])
print(f"\n Para invertir asi: {Convertida[::-1]}")
