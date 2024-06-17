print("\n************************")
print("string de teclado genera diccion. y dice cuantas veces se repite esa clave    *")
print("************************/n")

string = input("Ingresa un texto: ")
letters = dict.fromkeys(string,0)
for letra in string:
    letters[letra] += 1

print(letters)

















