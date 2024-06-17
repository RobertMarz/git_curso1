print("\n************************")
print("*   Programa Matrices con listas anidadas y for bucle_65*")
print("************************\n")
Matrix = [[1,2,3],[4,5,6],[7,8,9]]

Matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

print("CREAR UNA MATRIZ DE FILAxCOLUMNA rxc por teclado")
print("introduciendo los elementos por teclado y la filas y columnas")

#print(f"{Matrix[0]},\n{Matrix[1]},\n{Matrix[2]}")
#print(f"\nfila 1 columna 3  es el elemento: {Matrix[0][2]}")
#print("Imprimir matriz  usando for")
fila = int(input("Ingrese el numero de filas que desea: "))
columna = int(input("Ingrese el numero de columnas que desea: "))
Matriz = []
print("LLENADO DE MATRIZ")
for row in range(fila):
    ListaVacia = []
    for colu in range(columna):
        ListaVacia.append(int(input(f"Ingrese el elem de la fila -> {row+1} :")))
    Matriz.append(ListaVacia)

for row in Matriz:
    print(row)
    
    
