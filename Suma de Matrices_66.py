print("\n************************")
print("*  Suma de Matrices con listas anidadas y for bucle_65*")
print("************************\n")
MatrixA = [[1,2,3],[4,5,6],[7,8,9]]

MatrixB = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(MatrixA)
print(MatrixB)
print()
for row in range(len(MatrixA)):
    print(f"{MatrixA[row]}  {MatrixB[row]}")

print("Sumar las dos Matrices")

MatrizSuma = []

for row in range(len(MatrixA)):
    ListaNueva = []
    for colu in range(len(MatrixA[0])):
        ListaNueva.append(MatrixA[row][colu]+MatrixB[row][colu])
    MatrizSuma.append(ListaNueva)

for row in range(len(MatrixA)):
    print(f"{MatrixA[row]} + {MatrixB[row]} + {MatrizSuma[row]}")
    
