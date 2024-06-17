print("\n************************")
print("*   Matrices con listas anidadas y for bucle*")
print("************************\n")
Matrix = [[1,2,3],[4,5,6],[7,8,9]]

Matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
"""Para imprimir la lista anidada o matriz """
print(Matrix)
print()
"""Para imprimir como matriz """
print(f"{Matrix[0]},\n{Matrix[1]},\n{Matrix[2]}")
print(f"\nfila 1 columna 3  es el elemento: {Matrix[0][2]}")
print("Imprimir matriz  usando for")

for row in Matrix:
    print(f"\nfila : {row}")

print("Imprimir matriz  usando for otro modo")
for row in Matrix:
    for element in row:
        print(element, end = " ") # si le quitamos el edn imprime todo en columna

    print()
        
    
    
