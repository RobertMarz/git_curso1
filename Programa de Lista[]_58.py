print("\n************************")
print("*  PROGRAMA DE LISTAS *")
print("************************\n")

largo = int(input("Dame la longitud de tu lista : "))
numeros = []
for _ in range(largo):
    numeros.append(int(input("Introduce un numero entero : ")))

print(f"\n Lista numeros; {numeros} \n suma total es: {sum(numeros)}")
    

