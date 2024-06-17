print("\n************************")
print("*  Suma de Matrices cualquier cantidad por teclado_67*")
print("************************\n")
numero_de_matrices = int(input("Ingrese Nro, de matrices a Sumar: "))

if numero_de_matrices > 1:
    rows = int(input("Cuantas filas tendran tus matrices: "))
    columns = int(input("Cuantas columnas tendran tus matrices: "))

    matrix_list = []


    #Lle nado de matrices
    for number in range(numero_de_matrices):
        matrix = [] # por la cantidad de matrices
        #llenado de filas
        for row in range(rows):
            # nueva matriz para llevar el control de las columnas
            new_row = []
            #llenado de cada una de las matrices
            for column in range(columns):
                new_row.append(int(input(f"Ingresa un valor para la matriz {number+1} fila {row}, columna {column} : ")))

            matrix.append(new_row)
        matrix_list.append(matrix)
    #Suma de las matrices
    matrix = []
    for row in range(rows):
        new_row = []
        for column in range(columns):
            sum_matrix = 0
            for matrix_position in range(len(matrix_list )):
                sum_matrix += matrix_list[matrix_position][row][column]
            new_row.append(sum_matrix)
        matrix.append(new_row)
    matrix_list.append(matrix)

    #Imprimir matrices
    for matrix_row in range(rows):
        for matrix_list_position in range(len(matrix_list)):
            #
            if matrix_row != 1:
                print(f"{matrix_list[matrix_list_position][matrix_row]}", end="   ")
            else:
                if matrix_list_position < len(matrix_list)-2:
                    print(f"{matrix_list[matrix_list_position][matrix_row]}", end=" + ")
                elif matrix_list_position < len(matrix_list)-1:
                    print(f"{matrix_list[matrix_list_position][matrix_row]}", end=" = ")
                else:
                    print(f"{matrix_list[matrix_list_position][matrix_row]}", end=" ")
        print()
 
    
else:
    print("Se requiere dos o mas Matrices para realizar la suma")    

