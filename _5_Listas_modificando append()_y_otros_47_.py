print("\n************************")
print("*  MODIFICANDO Lista[] y Append()  *")
print("************************\n")

"""Método Acción
alumnos.append("Amaia") Inserta “Jon” al final de la lista
alumnos.insert(0,"Amaia") Inserta “Amaia” en la posición 0
alumnos.remove("Amaia") Elimina la primera aparición de “Amaia” de la lista
alumnos.pop() Elimina el último elemento de la lista
alumnos.clear() Elimina todos los elementos de la lista
alumnos.index("Amaia") Devuelve el índice de la primera aparición de
“Amaia”
alumnos.sort() Ordena la lista (los elementos deben ser
comparables)
sorted(alumnos) Devuelve una copia de la lista ‘alumnos’ ordenada
(no ordena la pasada como parámetro)
alumnos.reverse() Ordena la lista en orden inverso
alumnos.copy() Devuelve una copia de la lista
alumnos.extend(otra_lista) Fusiona las dos listas """

print("Lista Homogeneas \n")
vocales = ["a","e","i","o","u"]
print(vocales)
vocales[0] = "x"
print(vocales)
print(vocales[-1]) # ULTIMO ELEMENTO
vocales[2:4] = ["x","Y"]
print(vocales)
vocales = ["a","e","i","o","u"]
vocales[1:4] = ["x","Y","z"]
print(vocales)
print("AGREGANDO MAS ELEMENTOS")
vocales.append("LL")
print(f" nuevo elemento {vocales}")
vocales.append("S")
vocales.append("s1")
vocales.append(1.2)
vocales.append(True)
print(f" nuevo elemento {vocales}")
vocales = ["A","E","I","O","U"]
print(vocales)
vocales.append("a")
print(f" nuevo elemento {vocales}")
vocales.insert(2,'e')
print(f" insert e new elemento {vocales}")
vocales.remove('U')
print(f" remove U elemento {vocales}")
vocales.pop()
print(f" remove ultimo elemento {vocales}")
vocales.index('I')
print(f" da el indice de elemento {vocales.index('I')}")
vocales.sort()
print(f" Ordena los elementos {vocales}")
vocales.reverse()
print(f" Ordena en reverso los elementos {vocales}")
copia = vocales.copy()
print(f" Esta es Copia {copia}")
vocales.extend(copia)
print(f" Esta es Copia {vocales}")
vocales1 = sorted(copia)
print(f" Copia Ordenada {vocales1}")

