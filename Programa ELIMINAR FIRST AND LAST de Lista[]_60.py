print("\n************************")
print("*  PROGRAMA ELIMINAR PRIMERO Y ULTIMO DE LA LISTAS *")
print("************************\n")

NUMEROS = [1,2,3,4,5]
print(f"\n Lista Original {NUMEROS}")
NUMERO_ELI = []
NUMERO_ELI.append(NUMEROS.pop(0))
NUMERO_ELI.append(NUMEROS.pop())
#NUMERO_ELI.append(NUMEROS.pop(-)) elimina tambien el ultimo
print(f"\n Lista resultante {NUMEROS}")
print(f"\n Lista numeros eliminados {NUMERO_ELI}")
