print("\n************************")
print("*  METODO  reverse() y sort() DE LISTAS *")
print("************************\n")


vocales = ["a","e","i","o","u"]
print(f"Lista Original {vocales}")
vocales.reverse()
print(f"\n Lista Invertida {vocales}")

numeros = [4,5,3,1,2]
print(f"Lista Original de numeros {numeros}")
print(f"Lista Original de vocales {vocales}")
numeros.sort(reverse = True)
vocales.sort()
print(f"\n Lista Ordenada de numeros {numeros}")
print(f"Lista Ordenada de vocales {vocales}")
